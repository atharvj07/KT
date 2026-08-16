
// package com.company;

import java.util.Scanner;
import java.util.Stack;

public class Main {
    static Scanner input = new Scanner(System.in);

    private static void solve() {
        
        int n = input.nextInt();

        int[] p = arrayInput(n);
        input.close();
        
        // Map<Integer, Integer> map = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        char[] ans = new char[n*2];
        int indexAns = 0;
        int indexStack = 0;

        for (int i=0; i<n; i++) {
            while (stack.isEmpty() || stack.peek()<p[i]) {
                ans[indexAns++] = '(';
                stack.push(++indexStack);
            }
            if (stack.peek() != p[i]) {
                System.out.println(":(");
                return;
            }
            stack.pop();
            ans[indexAns++] = ')';
        }

        if(stack.size() >=1) {
            System.out.println(":(");
            return;
        } else {
            System.out.println(ans);
        }
        
    }

    public static void main(String[] args) {
        solve();
    }
    

    private static int[] arrayInput(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
        a[i] = input.nextInt();
        return a;
    }
}
