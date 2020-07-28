/*
    Problem
    As the football coach at your local school, you have been tasked with
    picking a team of exactly P students to represent your school. 
    
    There are N students for you to pick from. 
    The i-th student has a skill rating Si, which is a positive integer 
    indicating how skilled they are.

    You have decided that a team is fair if it has exactly P 
    students on it and they all have the same skill rating. 
    That way, everyone plays as a 
    team. Initially, it might not be possible to pick a fair team, 
    so you will give some of the students one-on-one coaching. 

    It takes one hour of coaching to increase the skill rating of any 
    student by 1.

    The competition season is starting very soon (in fact, the first match has already started!), 
    so you'd like to find the minimum number of hours of coaching you 
    need to give before you are able to pick a fair team.

    Input
    The first line of the input gives the number of test cases, T. 
    T test cases follow. 
    
    Each test case starts with a line containing the two 
    integers N and P, the number of students and the number of students 
    you need to pick, respectively. 
    
    Then, another line follows containing N integers Si; 
    the i-th of these is the skill of the i-th student.

*/

#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{
    string name = "t_training.txt";
    // fstream cin(name);

    int testcases, testcase = 1;
    cin >> testcases;
    cin.ignore();

    // cout << "testcases: " << testcases << endl;
    while (testcase <= testcases)
    {

        string line, word;
        int N, P;

        getline(cin, line);
        istringstream ss(line);

        ss >> N;
        ss >> P;

        // cout << "N, P: " << N << "  " << P << endl;

        getline(cin, line);
        ss = istringstream(line);
        vector<int> skill_counts(10001, 0);
        bool hit = false;

        while (ss >> word)
        {
            int v = stoi(word);
            skill_counts[v]++;
            // cout << "adding 1 to skill level: " << v << endl <<
            // "gives total players: " << skill_counts[v] << endl;

            if (skill_counts[v] >= P)
            {
                hit = true;
                break;
            }
        }

        if (hit) {
            cout << "Case #" << testcase << ": " << int(0) << endl;
            testcase++;
            continue;
        }

        // no hit
        long training_hours = -1;
        for (int ranki = 1; ranki < skill_counts.size(); ++ranki)
        {
            int need = P - skill_counts[ranki];  // num players
            if (need == P) continue;  // no players even at this level...

            long thours = 0;

            // cout << "ranki, need: " << ranki << " " << need << endl;

            for (int inner = ranki - 1; inner > 0 && need > 0; --inner)
            {

                int available = skill_counts[inner];
                int taking = available > need ? need : available;
                need -= taking;
                // cout << "inner, available, taking, need" <<
                // inner << " " << available << " " << taking << " "
                // << need << endl;

                int hours = ranki - inner;  // hours per player
                thours += hours * taking;
            }
            if (need == 0 && (training_hours == -1 || thours < training_hours))
            {
                training_hours = thours;
            }
        }
        cout << "Case #" << testcase << ": " << training_hours << endl;
        testcase++;
    }
    
    return 0;
}