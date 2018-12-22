class Solution {
public:

    // 123 % 10  = 3; 123 / 10 = 12
    // INT_MAX, INT_MIN   or can compared with them to check overflow

    int reverse(int x) {

        // can set long for 32 bit
        int result = 0;

        while (x != 0) {
            int tail = x % 10;
            int newresult = result * 10 + tail;
            if ((newresult - tail) / 10 != result) { 
                // different result if overflow
                return 0;
            }
            result = newresult;
            x = x / 10;
        }
        return result;
    }
};