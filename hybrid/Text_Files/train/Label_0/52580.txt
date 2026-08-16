

// package com.company;

import java.util.*;
import java.io.*;

public class Main {
    static Scanner input = new Scanner(System.in);


    public static void main(String[] args) {
        String ans = "";
        int n = input.nextInt();
        int p = input.nextInt();

        while (n != 0 || p!= 0) {
            int[] arr = new int[n];
            Arrays.fill(arr, 0);

            int index = 0;
            int stones = p; // stones in the glass
            while (arr[index] < p) {
                if (stones > 0) {
                    arr[index]++; // ứng viên đc nhận thêm 1 viên đá và chuyển cốc cho ng kế tiếp
                    if (arr[index] == p) break;
                    stones --;
                } else {
                    // Neu coc rong, ung vien phai bo het da vao coc
                    stones = arr[index];
                    arr[index] = 0;
                }
                index ++; // chuyen coc cho ng ke ben
                if (index ==  n) index = 0;
            }
            ans += "" + index + "\n";
            n = input.nextInt();
            p = input.nextInt();
        }
        
        System.out.println(ans.trim());
    }
}
