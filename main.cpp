#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

int algo(int cardNumber, int cardWidth, int cardHeight){
    int biggerSide = (cardWidth > cardHeight) ? cardWidth : cardHeight; 
    int smallerSide = cardWidth + cardHeight - biggerSide; 

    int exceptionSideSize = biggerSide * cardNumber; 
    int oldTemp = exceptionSideSize; 
    int temp = 0;

    if (cardNumber == 1){                   
        return biggerSide;
    }
    if (cardWidth == cardHeight){             
        return ceil(sqrt(cardNumber)) * cardWidth;
    }
     for (int i = 1; i < ceil(cardNumber/2); ++i){                        
        if (cardNumber % i == 0){
            temp = (smallerSide * (cardNumber / i) > biggerSide * i) ? smallerSide * (cardNumber / i) : biggerSide * i;
            exceptionSideSize = (temp < oldTemp) ? temp : oldTemp;
            oldTemp = temp;
        }
    }

    int maxSideSize = 0;
    int finalSideSize = 0;
    int rowNumber = 1;

    for (int columnNumber = cardNumber; columnNumber > 1; --columnNumber){    
        if (columnNumber == cardNumber / rowNumber && rowNumber != 1){
            rowNumber++;
        }

        maxSideSize = (smallerSide * columnNumber > biggerSide * rowNumber) ? smallerSide * columnNumber : biggerSide * rowNumber;

        if (finalSideSize > maxSideSize){
            finalSideSize = maxSideSize;
        }

        if (columnNumber == cardNumber){
            rowNumber++;
            finalSideSize = maxSideSize;
        }
    }

    return (finalSideSize < exceptionSideSize) ? finalSideSize : exceptionSideSize; 
}

int main(){
    int cardNumber, cardWidth, cardHeight;

    fstream bugtracker_in;
    bugtracker_in.open("bugtracker_in", ios::in);
    if (!bugtracker_in){
        cout << "Does not exist!";
        return 0;
    }
    bugtracker_in >> cardNumber;
    bugtracker_in >> cardWidth;
    bugtracker_in >> cardHeight;
    bugtracker_in.close();

    int tableSide = algo(cardNumber, cardWidth, cardHeight);

    fstream bugtracker_out;
    bugtracker_out.open("bugtracker_out", ios::out);
    if (!bugtracker_out){
        cout << "Does not exist!";
        return 0;
    }
    bugtracker_out << tableSide << endl;
    bugtracker_out.close();

    cout << cardNumber << " " <<  cardWidth << " " << cardHeight << "\n" << tableSide << endl;
    return 0;
}