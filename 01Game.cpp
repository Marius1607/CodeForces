/*01 Game
Alica and Bob are playing a game.

Initially they have a binary string s consisting of only characters 0 and 1.

Alice and Bob make alternating moves: Alice makes the first move, Bob makes the second move, Alice makes the third one, and so on.
 During each move, the current player must choose two different adjacent characters of string s and delete them.
 For example, if s=1011001 then the following moves are possible:

 */
#include <bits/stdc++.h>


int minim(int x, int y){
    return (x < y)?x:y;
}

int main()
{
    int n;
    char s[100];
    scanf("%d",&n);
    while(n--){
        int a = 0, b = 0;
        scanf("%s",s);
        for(int i = 0; i<strlen(s); i++)
        {
            s[i] == '0' ? a++ : b++;
        }
        minim(a,b) % 2 ? printf("DA\n") : printf("NET\n");
    }
    return 0;
}
