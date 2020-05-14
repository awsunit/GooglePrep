/*
    Palindromes

    Given a line of N blocks:
    for q questions:
        range_of_blocks = {Li,Ri}

        if(makesPalindrome(L,R,blocks)
            canAnswer++;
*/
#include <cerrno>
#include <iostream>
#include <vector>
#include <cstdbool>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;

bool matching(int left, int right, vector<char>& blocks);

int main(int argc, char **argv) {

    // # test cases
    int cases;
    cin >> cases;
    

    cout << "cases given: " << cases << endl;


    for (int c = 0; c < cases; c++){

        cout << "starting case: #" << c << endl;

        // how many palindromes have we made this case
        int canAnswer = 0;

        int num_questions;
        int num_blocks;
        string input;

        cin >> input;

        auto it = input.cbegin();
        num_blocks = std::stoi(input.substr(0,1));
        num_questions = std::stoi(input.substr(1));

        cout << "blocks and q's: " << num_blocks << num_questions << endl;

        // get the blocks
        string string_blocks;
        vector<char> og_blocks;
        char nc;

        cin >> string_blocks;

        // insert 0 for working with input style
        og_blocks.push_back(char(0));
        for (auto it=string_blocks.cbegin(); it != string_blocks.cend(); ++it) {
            og_blocks.push_back(*it);
        }

        // check content
        for (auto it=og_blocks.cbegin(); it != og_blocks.cend(); ++it) {
            cout << *it << " ";
        }
        cout << endl;
        
        for (int question = 0; question < num_questions; question++) {
            int left, right;
            cin >> string_blocks;
            auto it = string_blocks.cbegin();
            left = std::stoi(string_blocks.substr(0,1));
            right = std::stoi(string_blocks.substr(1));
            vector<char> blocks = og_blocks;

            bool ok = true;
            while (right > left) {
                // find us a match
                if (!matching(left, right, blocks)) {
                    ok = false;
                    break;
                }
                left++;
                right--;
            }

            if (ok) {
                canAnswer++;
            }     
        }   // end-q's

        cout << "Case #" << c << ": " << canAnswer << endl;

    }  // end-cases

    return EXIT_SUCCESS;
}

bool matching(int left, int right, vector<char>& blocks) {
    int og_right = right;
    while (right > left) {
        if (blocks.at(right) == blocks.at(left)) {
            // swap values, return
            char t = blocks.at(og_right);
            blocks.at(og_right) = blocks.at(right);
            blocks.at(right) = t;
            return true;
        }
        right--;
    }
    return false;
}