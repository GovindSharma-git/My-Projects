#include <iostream>
#include <vector>
using namespace std;
int q=0;
bool Tic(vector<vector<int>> &v, int x, int y, int p)
{
    if (x >= 3 || y >= 3)
    {
        cout <<endl<< "Invalid Input! Play Again" << endl<<endl;
        q=p;
        return false;
    }
    if (p == 1 && v[x][y] != 79 && v[x][y] != 88)
        v[x][y] = 79;
    else if (p == 2 && v[x][y] != 79 && v[x][y] != 88)
        v[x][y] = 88;
    else
    {
        cout << endl<<"Invalid Input! Play Again" << endl<<endl;
        q=p;
        return false;
    }
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << (char)v[i][j] << " ";
        }
        cout << endl;
    }
    if (v[0][0] == v[1][1] && v[1][1] == v[2][2] && v[0][0] != 32 && v[1][1] != 32 && v[2][2] != 32){
        if(v[0][0]==79) cout<<"First player ";
        else cout<<"Second Player ";
        return true;
    }
    else if (v[0][2] == v[1][1] && v[1][1] == v[2][0] && v[0][2] != 32 && v[1][1] != 32 && v[2][0] != 32){
        if(v[0][2]==79) cout<<"First player ";
        else cout<<"Second Player ";
        return true;
    }
    else if (v[0][0] == v[0][1] && v[0][1] == v[0][2] && v[0][0] != 32 && v[0][1] != 32 && v[0][2] != 32){
        if(v[0][0]==79) cout<<"First player ";
        else cout<<"Second Player ";
        return true;
    }
    else if (v[1][0] == v[1][1] && v[1][1] == v[1][2] && v[1][0] != 32 && v[1][1] != 32 && v[1][2] != 32){
        if(v[1][0]==79) cout<<"First player ";
        else cout<<"Second Player ";
        return true;
    }
    else if (v[2][0] == v[2][1] && v[2][1] == v[2][2] && v[2][0] != 32 && v[2][1] != 32 && v[2][2] != 32){
        if(v[2][0]==79) cout<<"First player ";
        else cout<<"Second Player ";
        return true;
    }
    else if (v[0][0] == v[1][0] && v[1][0] == v[2][0] && v[0][0] != 32 && v[1][0] != 32 && v[2][0] != 32){
        if(v[0][0]==79) cout<<"First player ";
        else cout<<"Second Player ";
        return true;
    }
    else if (v[0][1] == v[1][1] && v[1][1] == v[2][1] && v[0][1] != 32 && v[1][1] != 32 && v[2][1] != 32){
        if(v[0][1]==79) cout<<"First player ";
        else cout<<"Second Player ";
        return true;
    }
    else if (v[0][2] == v[1][2] && v[1][2] == v[2][2] && v[0][2] != 32 && v[1][2] != 32 && v[2][2] != 32){
        if(v[0][2]==79) cout<<"First player ";
        else cout<<"Second Player ";
        return true;
    }
}
int main()
{
    vector<vector<int>> v(3, vector<int>(3, 32));
    int x, y;
    bool flag = false;
    int m=0;
    cout<<"Let's Play Tic-Tac-Toe all you need is one more bro!"<<endl<<"Rules: "<<endl<<"1. You have to type the index of matrix in which you want to put your next move."<<endl;
    cout<<"2. The first Player will be automatically assinged a 'O' character and second player 'X' So choose your position wisely before starting the game!"<<endl;
    cout<<"3. You are allowed to put the index value between 1 and 3 only and you should not overwrite a particular index."<<endl;
    cout<<endl;
    while (flag == false)
    {
        if(q==0){
        cout << "First Player Turn : ";
        cin >> x >> y;
        flag = Tic(v, x - 1, y - 1, 1);
        }
        else q=0;
        if (flag == false)
        {
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    if (v[i][j] != 32)
                        flag = true;
                    else
                    {
                        flag = false;
                        break;
                    }
                }
            }
            if (flag == true){
                cout << "Tie";
                m=1;
            }
        }
        if (flag == false)
        {
            if(q==0){
            cout << "Second Player Turn : ";
            cin >> x >> y;
            flag = Tic(v, x - 1, y - 1, 2);
            }
            else q=0;
        }
    }
    if(m==0) cout << "Win";
}