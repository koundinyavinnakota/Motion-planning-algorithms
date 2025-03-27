#include <opencv2/opencv.hpp>
#include <iostream>

// Create map with obstacles
cv::Mat get_map(int c = 5) {
    cv::Mat layout = cv::Mat::zeros(100 * c, 100 * c, CV_8UC3);

    // Obstacle 1
    std::vector<cv::Point> obs1 = {
        cv::Point(25 * c, 100 * c),
        cv::Point(25 * c, 10 * c),
        cv::Point(30 * c, 10 * c),
        cv::Point(30 * c, 100 * c)
    };
    cv::fillPoly(layout, std::vector<std::vector<cv::Point>>{obs1}, cv::Scalar(255, 255, 255));

    // Obstacle 2
    std::vector<cv::Point> obs2 = {
        cv::Point(75 * c, 0),
        cv::Point(75 * c, 90 * c),
        cv::Point(80 * c, 90 * c),
        cv::Point(80 * c, 0)
    };
    cv::fillPoly(layout, std::vector<std::vector<cv::Point>>{obs2}, cv::Scalar(255, 255, 255));

    return layout;
}

// Draw start node (green circle)
void set_start_node(cv::Mat& map, int x, int y) {
    cv::circle(map, cv::Point(x, y), 5, cv::Scalar(0, 255, 0), -1);
}

// Draw goal node (red circle)
void set_goal_node(cv::Mat& map, int x, int y) {
    cv::circle(map, cv::Point(x, y), 5, cv::Scalar(0, 0, 255), -1);
}

// Check if the given point is in an obstacle (white)
bool isObstacle(const cv::Mat& map, int x, int y) {
    cv::Vec3b pixel = map.at<cv::Vec3b>(y, x);  // (row, col) = (y, x)
    return (pixel[0] == 255 && pixel[1] == 255 && pixel[2] == 255);
}

int main() {
    int c = 5;
    cv::Mat map = get_map(c);

    int startX = 20 * c;
    int startY = 20 * c;
    int goalX = 85 * c;
    int goalY = 85 * c;

    set_start_node(map, startX, startY);
    set_goal_node(map, goalX, goalY);

    std::cout << "Is (" << startX << ", " << startY << ") an obstacle? " 
              << (isObstacle(map, startX, startY) ? "Yes" : "No") << std::endl;

    cv::imshow("Map", map);
    cv::waitKey(0);
    return 0;
}
