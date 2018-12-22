#include "gtest/gtest.h"
#include "ReverseInteger.cpp"


TEST(ReverseInteger, Test1) {
    Solution sol;

    int x1 = 123;
    int target1 = 321;
    int res1 = sol.reverse(x1);
    ASSERT_EQ(target1, res1);
}

TEST(ReverseInteger, Test2) {
    Solution sol;

    int x2 = -123;
    int target2 = -321;
    int res2 = sol.reverse(x2);
    ASSERT_EQ(target2, res2);
}

TEST(ReverseInteger, Test3) {
    Solution sol;

    int x3 = 120;
    int target3 = 21;
    int res3 = sol.reverse(x3);
    ASSERT_EQ(target3, res3);
}


// overflow
TEST(ReverseInteger, Test4) {
    Solution sol;

    int x4 = 2147483647;
    int target4 = 0;
    int res4 = sol.reverse(x4);
    ASSERT_EQ(target4, res4);
}