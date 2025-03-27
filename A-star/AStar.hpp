#ifndef ASTAR_HPP
#define ASTAR_HPP

#include "Node.hpp"
#include <opencv2/opencv.hpp>
#include <queue>
#include <vector>
#include <cmath>
#include <iostream>

struct Compare {
    bool operator()(const std::pair<double, Node*>& a, const std::pair<double, Node*>& b) {
        return a.first > b.first;
    }
};

bool checkInClosed(const std::vector<Node*>& closedlist, Node* node) {
    for (const auto& n : closedlist) {
        if (*n == *node) return true;
    }
    return false;
}

double calculateTotalCost(Node* node, Node* goal, double c2c) {
    node->g = c2c + (node->parent ? node->parent->g : 0);
    node->h = std::sqrt(std::pow(node->x - goal->x, 2) + std::pow(node->y - goal->y, 2));
    node->f = node->g + node->h;
    return node->f;
}

std::vector<Node*> astar(Node* start, Node* goal, cv::Mat& map) {
    std::vector<Node*> closed;
    std::priority_queue<std::pair<double, Node*>, std::vector<std::pair<double, Node*>>, Compare> open;

    const std::vector<std::pair<int, int>> moves = {
        {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}
    };
    const std::vector<double> costs(8, 1.0); // uniform cost

    open.push({0.0, start});
    bool goal_reached = false;

    while (!open.empty() && !goal_reached) {
        auto cur = open.top();
        open.pop();

        for (size_t i = 0; i < moves.size(); ++i) {
            int nx = cur.second->x + moves[i].first;
            int ny = cur.second->y + moves[i].second;

            if (nx >= 0 && nx < map.cols && ny >= 0 && ny < map.rows &&
                map.at<cv::Vec3b>(ny, nx) != cv::Vec3b(255, 255, 255)) {

                Node* next = new Node(nx, ny);
                next->updateParent(cur.second);

                if (*next == *goal) {
                    std::cout << "🎯 Goal Reached!\n";
                    goal->updateParent(cur.second);
                    goal_reached = true;
                    break;
                }

                if (checkInClosed(closed, next)) {
                    delete next;
                    continue;
                }

                open.push({calculateTotalCost(next, goal, costs[i]), next});
                cv::circle(map, cv::Point(nx, ny), 0, cv::Scalar(255, 0, 0), -1);
                cv::imshow("exploration", map);
                cv::waitKey(1);
            }
        }

        closed.push_back(cur.second);
    }

    if (goal_reached) {
        closed.push_back(goal);
    }

    return closed;
}

#endif
