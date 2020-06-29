/* Shovels and Swords
Polycarp plays a well-known computer game (we won't mention its name). In this game, he can craft tools of two types — shovels and swords.
To craft a shovel, Polycarp spends two sticks and one diamond; to craft a sword, Polycarp spends two diamonds and one stick.

Each tool can be sold for exactly one emerald. How many emeralds can Polycarp earn, if he has a sticks and b diamonds?
*/
#include <bits/stdc++.h>
#define min(x,y,z) (x < y ? (x < z ? x : z) : (y < z ? y : z))

int main()
{
    int cases;
    scanf("%d", &cases);
    int s,d,m;
    while(cases--){
         scanf("%d %d", &d,&s);
         printf("%d\n", min(d,s,(d+s)/3));
    }
    return 0;
}

