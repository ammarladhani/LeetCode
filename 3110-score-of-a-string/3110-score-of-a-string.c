int scoreOfString(char* s) {
    int i = 1;
    int score = 0;
    while(s[i]) {
        int adding = s[i]-s[i-1];
        if(adding < 0) {
            adding *= -1;
        }
        score+=adding;
        i++;
    }
    return score;
}