#include "Node.hpp"
#include "AStar.hpp"
#include <opencv2/opencv.hpp>
#include <vector>
#include <chrono>

void set_start_node(cv::Mat& map, int x, int y) {
    cv::circle(map, cv::Point(x, y), 3, cv::Scalar(0, 255, 0), -1);
}

void set_goal_node(cv::Mat& map, int x, int y) {
    cv::circle(map, cv::Point(x, y), 3, cv::Scalar(0, 0, 255), -1);
}

cv::Mat get_map(int c = 5) {
    cv::Mat layout = cv::Mat::zeros(100 * c, 100 * c, CV_8UC3);

    std::vector<cv::Point> obs1 = {
        cv::Point(25 * c, 100 * c),
        cv::Point(25 * c, 10 * c),
        cv::Point(30 * c, 10 * c),
        cv::Point(30 * c, 100 * c)
    };
    cv::fillPoly(layout, std::vector<std::vector<cv::Point>>{obs1}, cv::Scalar(255, 255, 255));

    std::vector<cv::Point> obs2 = {
        cv::Point(75 * c, 0),
        cv::Point(75 * c, 90 * c),
        cv::Point(80 * c, 90 * c),
        cv::Point(80 * c, 0)
    };
    cv::fillPoly(layout, std::vector<std::vector<cv::Point>>{obs2}, cv::Scalar(255, 255, 255));

    return layout;
}

void backtrack(Node* node, Node* start, std::vector<std::pair<int, int>>& path) {
    path.push_back(node->current_node());
    if (node->parent && *node->parent == *start) {
        path.push_back(start->current_node());
        return;
    }
    if (node->parent)
        backtrack(node->parent, start, path);
}

void plotPath(const std::vector<std::pair<int, int>>& path, cv::Mat& map) {
    for (const auto& p : path) {
        cv::circle(map, cv::Point(p.first, p.second), 0, cv::Scalar(0, 255, 0), -1);
        cv::imshow("path", map);
        cv::waitKey(1);
    }
}

int main() {
    auto start_time = std::chrono::high_resolution_clock::now();

    cv::Mat map = get_map(1);
    Node* start_node = new Node(5, 95);
    Node* goal_node = new Node(95, 5);

    set_start_node(map, start_node->x, start_node->y);
    set_goal_node(map, goal_node->x, goal_node->y);

    std::vector<Node*> closed_list = astar(start_node, goal_node, map);
    std::vector<std::pair<int, int>> path_found;
    backtrack(goal_node, start_node, path_found);

    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end_time - start_time;
    std::cout << "⏱️ Total Time: " << duration.count() << " seconds\n";

    plotPath(path_found, map);
    cv::waitKey(0);
    return 0;
}
