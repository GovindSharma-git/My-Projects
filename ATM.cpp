#include <iostream>
using namespace std;
int main()
{
    int pin;
    cout << "Welcome!" << endl
         << "Enter your 4 digit pin : ";
    cin >> pin;
    if (pin != 1234)
        cout << "Incorrect pin!" << endl
             << "Your ATM is blocked for 24 hours";
    else
    {
        int ui = 1;
        int Bal = 210938;
        while (ui != 4)
        {
            cout << "Check Balance(Press 1)" << endl
                 << "Withdraw Money(Press 2)" << endl
                 << "Deposit Money(Press 3)" << endl
                 << "Exit(Press 4)" << endl;
            cin >> ui;
            if (ui == 0 || ui > 4)
            {
                cout << "Invalid Input";
                continue;
            }
            else if (ui == 1)
            {
                cout << "You Balance is : " << Bal<<endl;
                cout << "Thank You!"<<endl;
            }
            else if (ui == 2)
            {
                int w;
                cout << "Enter Amount to Withdraw : ";
                cin >> w;
                Bal -= w;
                cout << "Collect your Money"<<endl;
                cout << "Thank You!"<<endl;
            }
            else if (ui == 3)
            {
                int d;
                cout << "Enter Amount to Deposit : ";
                cin >> d;
                Bal += d;
                cout << "Deposit your Money"<<endl;
                cout << "Thank You!"<<endl;
            }
            else{
                cout << "Thank You!";
                break;
            }
            bool flag;
            cout<<"Do you want to exit?"<<"Press 1 for Yes and Press 0 for No"<<endl;
            cin>>flag;
            if(flag==false){
                cout << "Thank You!";
                break;
            }
        }
    }
}