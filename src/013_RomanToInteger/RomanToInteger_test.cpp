#include "gtest/gtest.h"
#include "RomanToInteger.cpp"

TEST(RomanToInteger, TestA) {
    Solution sol;
    string str1 = "";
    int res1 = sol.romanToInt(str1);
    int target1 = 0;
    ASSERT_EQ(res1, target1);
}

TEST(RomanToInteger, TestB) {
    Solution sol;
    string str2 = "DCXXI";
    int res2 = sol.romanToInt(str2);
    int target2 = 621;
    ASSERT_EQ(res2, target2);
}


TEST(RomanToInteger, TestC) {
    Solution sol;
    string str3 = "X";
    int res3 = sol.romanToInt(str3);
    int target3 = 10;
    ASSERT_EQ(res3, target3);
}