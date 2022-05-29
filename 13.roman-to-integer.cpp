/*
 * @lc app=leetcode id=13 lang=cpp
 *
 * [13] Roman to Integer
 */

// @lc code=start
class Solution {
public:
    int romanToInt(string s) {
        int answer = 0;
        for (int i = 0; i < s.length(); i++) {
            switch (s[i]) {
                case 'I':
                    if (i + 1 != s.length()) {
                        if (s[i + 1] == 'V' || s[i + 1] == 'X') {
                            answer--;
                            break;
                        }
                    }
                    answer++;
                    break;

                case 'V':
                    answer += 5;
                    break;

                case 'X':
                    if (i + 1 != s.length()) {
                        if (s[i + 1] == 'L' || s[i + 1] == 'C') {
                            answer -= 10;
                            break;
                        }
                    }
                    answer += 10;
                    break;

                case 'L':
                    answer += 50;
                    break;

                case 'C':
                    if (i + 1 != s.length()) {
                        if (s[i + 1] == 'D' || s[i + 1] == 'M') {
                            answer -= 100;
                            break;
                        }
                    }
                    answer += 100;
                    break;

                case 'D':
                    answer += 500;
                    break;

                case 'M':
                    answer += 1000;
                    break;

                default:
                    break;
            }
        }

        return answer;
    }
};
// @lc code=end
