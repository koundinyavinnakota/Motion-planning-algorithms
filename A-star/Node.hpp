#ifndef NODE_HPP
#define NODE_HPP

#include <cmath>

struct Node {
    int x, y;
    double f, g, h;
    Node* parent;

    Node(int x_, int y_) : x(x_), y(y_), f(0), g(0), h(0), parent(nullptr) {}

    std::pair<int, int> current_node() const {
        return {x, y};
    }

    void updateParent(Node* p) {
        parent = p;
    }

    bool operator==(const Node& other) const {
        return current_node() == other.current_node();
    }

    // For priority queue
    bool operator>(const Node& other) const {
        return f > other.f;
    }
};

#endif
