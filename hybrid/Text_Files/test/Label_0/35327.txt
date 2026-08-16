

import java.util.Scanner;

public class Elevator {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String floor=s.next();
        int pos=1;
        for (int i = 0; i < 2; i++) {
            switch (floor.charAt(i)){
            case '0':
                pos=pos*2;
                break;
            case '1':
                pos=pos*7;
                break;
            case '2':
                pos=pos*2;
                break;
            case '3':
                pos=pos*3;
                break;
            case '4':
                pos=pos*3;
                break;
            case '5':
                pos=pos*4;
                break;
            case '6':
                pos=pos*2;
                break;
            case '7':
                pos=pos*5;
                break;
            case '8':
                pos=pos*1;
                break;
            case '9':
                pos=pos*2;
                break;
            default:
                break;
            
            }
        
        }
        System.out.println(pos);
        pos=0;
    }
}
