#include <vector>

struct Foo {
  double x;
  int y;
};

std::vector<Foo> foos;

void bar(Foo& f) {
  f.x
}