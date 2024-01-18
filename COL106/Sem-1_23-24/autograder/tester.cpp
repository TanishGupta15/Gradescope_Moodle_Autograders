#include <bits/stdc++.h>
#include "Node.h"
#include "qna_tool.h"

using namespace std;

// TODO: Add segfault signal handler

int main(int argc, char** argv){

    std::string query_filename = argv[1];

    std::cout << "Running test case " << query_filename << std::endl;

    QNA_tool qna_tool;

    for(int i = 1; i <= 98; i++){

        // std::cout << "Inserting book " << i << std::endl;

        std::string filename = "corpus/mahatma-gandhi-collected-works-volume-";
        filename += to_string(i);
        filename += ".txt";

        std::ifstream inputFile(filename);

        if (!inputFile.is_open()) {
            std::cout << "Failed :(\n";
            std::cerr << "Error: Unable to open the input file mahatma-gandhi." << std::endl;
            return 0;
        }

        std::string tuple;
        std::string sentence;


        while (std::getline(inputFile, tuple, ')') && std::getline(inputFile, sentence)) {
            // Get a line in the sentence
            tuple += ')';

            std::vector<int> metadata;    
            std::istringstream iss(tuple);

            // Temporary variables for parsing
            std::string token;

            // Ignore the first character (the opening parenthesis)
            iss.ignore(1);

            // Parse and convert the elements to integers
            while (std::getline(iss, token, ',')) {
                // Trim leading and trailing white spaces
                size_t start = token.find_first_not_of(" ");
                size_t end = token.find_last_not_of(" ");
                if (start != std::string::npos && end != std::string::npos) {
                    token = token.substr(start, end - start + 1);
                }
                
                // Check if the element is a number or a string
                if (token[0] == '\'') {
                    // Remove the single quotes and convert to integer
                    int num = std::stoi(token.substr(1, token.length() - 2));
                    metadata.push_back(num);
                } else {
                    // Convert the element to integer
                    int num = std::stoi(token);
                    metadata.push_back(num);
                }
            }

            // Now we have the string in sentence
            // And the other info in metadata
            // Add to the dictionary

            // Insert in the qna_tool
            qna_tool.insert_sentence(metadata[0], metadata[1], metadata[2], metadata[3], sentence);
        }

        inputFile.close();

    }

    string question = "";

    // read question from file
    ifstream question_file(query_filename);
    if (!question_file.is_open()) {
        std::cout << "Failed :(\n";
        std::cerr << "Error: Unable to open the input file " << query_filename << "." << std::endl;
        return 0;
    }

    std::getline(question_file, question);

    // next line is the k
    int k;
    question_file >> k;

    // Let's try to ask a simple question to the qna_tool
    Node* head = qna_tool.get_top_k_para(question, k);
    // next 3*k lines are the answers

    vector<vector<int>> ans;

    for(int i = 0; i < k; i++){
        int a, b, c;
        question_file >> a >> b >> c;
        ans.push_back({a, b, c});
    }

    int cnt = 0;
    bool should_check_scores = false;
    Node* temp = head;
    while(temp != NULL){
        if(cnt >= k) {
            std::cout << "Failed :(\n";
            cerr << "More than " << k << " paragraphs returned" << endl;
            return 0;
        }

        if(temp->book_code != ans[cnt][0] || temp->page != ans[cnt][1] || temp->paragraph != ans[cnt][2]){
            // std::cout << "Failed :(\n";
            // cerr << "Wrong paragraph returned" << endl;
            // cerr << "Paragraph returned: " << temp->book_code << " " << temp->page << " " << temp->paragraph << endl;
            // cerr << "Paragraph expected: " << ans[cnt][0] << " " << ans[cnt][1] << " " << ans[cnt][2] << endl;
            // return 0;
            should_check_scores = true;
        }

        cnt++;
        temp = temp->right;
    }

    if(cnt < k){
        std::cout << "Failed :(\n";
        cerr << "Less than " << k << " paragraphs returned" << endl;
        return 0;
    }

    double precision_threshold = 0.0001;

    if(should_check_scores){
        string filename = "query_";
        // get query num from query_filename
        // remove .txt from end
        string query_num = query_filename.substr(6, query_filename.length() - 10);
        filename += query_num;
        filename += "_scores.txt";

        Node* t = head;
        int cnt = 0;
        // open scores file

        while(t != nullptr){
            if(t->book_code == ans[cnt][0] && t->page == ans[cnt][1] && t->paragraph == ans[cnt][2]){
                t = t->right;
                cnt++;
                continue;
            }

            ifstream scores_file(filename);
            if (!scores_file.is_open()) {
                std::cout << "Failed :(\n";
                std::cerr << "Error: Unable to open the input file " << filename << "." << std::endl;
                return 0;
            }

            // now need to check score
            // iterate through the entire file to find both the scores
            int book_code, page, paragraph;
            double score_expected, score_returned, score;
            bool found_expected = false, found_returned = false;
            while(scores_file >> book_code >> page >> paragraph >> score){
                if(book_code == ans[cnt][0] && page == ans[cnt][1] && paragraph == ans[cnt][2]){
                    score_expected = score;
                    found_expected = true;
                }
                if(book_code == t->book_code && page == t->page && paragraph == t->paragraph){
                    score_returned = score;
                    found_returned = true;
                }
                if(found_expected && found_returned) break;
            }
            if(!found_expected || !found_returned){
                std::cout << "Failed :(\n";
                // cerr << "Score not found" << endl;
                if(!found_expected) cerr << "Score not found for expected " << ans[cnt][0] << " " << ans[cnt][1] << " " << ans[cnt][2] << endl;
                if(!found_returned) cerr << "Score not found for returned " << t->book_code << " " << t->page << " " << t->paragraph << endl;
                return 0;
            }
            if(abs(score_expected - score_returned) > min(precision_threshold, score_expected * 1e-5)){ // this threshold should be fine
                std::cout << "Failed :(\n";
                cerr << "Wrong paragraph and score returned" << endl;
                cerr << "Score returned: " << fixed << setprecision(7) << score_returned << endl;
                cerr << "Score expected: " << fixed << setprecision(7) << score_expected << endl;
                cerr << "Difference in scores: " << fixed << setprecision(7) << abs(score_expected - score_returned) << endl;
                return 0;
            }
            scores_file.close();
            t = t->right;
            cnt++;
        }
    }

    std::cout << "Passed\n";
    cerr << "Passed\n" << endl;
    question_file.close();
    return 0;
}