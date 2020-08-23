#include <vector>
#include <iostream>
#include <unordered_set> 
#include <algorithm> 
#include <string>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::string;


class Femail {
public:
    int numUniqueEmails(vector<string>& emails) {
        int num = 0;
        std::unordered_set<string> nemails;

        for (auto& s : emails) {
            int l = s.find("@");
            string local = s.substr(0, l);
            string domain = s.substr(l);
            cout << "domain: " << domain << endl;

            int plus;
            if ((plus = local.find("+")) < local.length()) {
                local = local.substr(0, plus);
            }
            local = std::replace(local.begin(), local.end(), '.', "");
            cout << "local: " << local << endl;
            nemails.insert(nemails.end(), local + "@" + domain);
        }
        

        return nemails.size();
    }
};

int main() {

    Femail f;
    vector<string> emails = {"test.email+alex@leetcode.com",
                    "test.e.mail+bob.cathy@leetcode.com",
                    "testemail+david@lee.tcode.com"};

    cout << f.numUniqueEmails(emails) << endl;

    cout << "done" << endl;
    return 0;
}