/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
//package Contests;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

/**
 *
 * @author Akhilesh
 */
public class A1149 {
    public static void main(String[] args) throws IOException{
        BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(scan.readLine().trim());
        
        String str[] = scan.readLine().split("\\s+");
        
        int one = 0, two = 0;
        for(int i = 0; i < n; i++){
            if(str[i].equals("1")){
                one++;
            }else
                two++;
        }
        
        ArrayList<Integer> primes = sieve(one + two*2);
        int index = 0, currSum = 0;
        StringBuilder s = new StringBuilder();
        while(one > 0 && two > 0 && index < primes.size()){
            int prime = primes.get(index++);
            int diff = prime - currSum;
            currSum += diff;
            int numTwo = Math.min(two, diff/2);
            diff -= 2*numTwo;
            for(int i = 0; i < numTwo; i++){
                s.append("2 ");
            }
            two -= numTwo;
            int numOne = Math.min(one, diff);
            for(int i = 0; i < numOne; i++){
                s.append("1 ");
            }
            one -= numOne;
        }
        while(one-- > 0){
            s.append("1 ");
        }
        while(two-- > 0){
            s.append("2 ");
        }
        System.out.println(s);
    }
    
    static ArrayList<Integer> sieve(int n){ 
        boolean prime[] = new boolean[n+1]; 
        for(int i=0;i<=n;i++) 
            prime[i] = true;
        int count = n - 1;
        for(int p = 2; p*p <=n; p++){ 
            if(prime[p] == true){
                for(int i = p*p; i <= n; i += p){
                    prime[i] = false;
                    count--;
                }
            } 
        }
        ArrayList<Integer> list = new ArrayList<>();
        int index = 0;
        for(int i = 2; i <= n; i++) { 
            if(prime[i] == true)
                list.add(i);
        }
        
        return list;
    }
}
