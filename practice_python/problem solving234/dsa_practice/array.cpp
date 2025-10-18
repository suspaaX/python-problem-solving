#include <iostream>
using namespace std;

int main() {

    int  num [] = {10,45,87,98,-65};
    int size = 5;
    int smallest = INT_MAX;
    int largest = INT_MIN;

    for (int i=0; i<size; i++)

    {
        // if(num[i]<smallest){
        //     smallest = num[i];
        smallest = min(num[i],smallest);
        largest = max(num[i],largest);

    }
    cout<<"smallest = "<<smallest<<endl;
    cout<<"largest = "<<largest<<endl;
    return 0;
}