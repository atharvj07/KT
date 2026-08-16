//problem: https://codeforces.com/problemset/problem/1025/A

import java.util.Scanner;
import java.util.Arrays;

public class Doggo{
    public static void main(String[] args){
        Scanner sObj = new Scanner(System.in);
        int size = Integer.parseInt(sObj.nextLine());
        if(size==1){
            System.out.println("Yes");
            return;
        }
        int[] arr = new int[128];
        for(char c: sObj.nextLine().toCharArray()){
            arr[c]++;
            if(arr[c] >= 2){
                System.out.println("Yes");
                return;
            }
        }
        System.out.println("No");
    }
}