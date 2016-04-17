#include "cppjieba/Jieba.hpp"
#include "cppjieba/KeywordExtractor.hpp"

using namespace std;

const char* const DICT_PATH = "../dict/jieba.dict.utf8";
const char* const HMM_PATH = "../dict/hmm_model.utf8";
const char* const USER_DICT_PATH = "../dict/user.dict.utf8";
const char* const IDF_PATH = "../dict/idf.utf8";
const char* const STOP_WORD_PATH = "../dict/stop_words.utf8";

int main(int argc, char** argv) {
  cppjieba::QuerySegment jieba(DICT_PATH,
        HMM_PATH,
        USER_DICT_PATH);
  vector<string> words;
  string result;
  string s;
    for(int i = 1; i < argc; ++i){
        s += string(argv[i]);
    }

  jieba.Cut(s, words, true);
  cout << limonp::Join(words.begin(), words.end(), "/") << endl;
  return EXIT_SUCCESS;
}
