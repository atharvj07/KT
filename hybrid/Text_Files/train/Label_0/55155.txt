//package SecondSemester;


import java.lang.*;
import java.util.*;
import java.lang.Math;

public class HDD {
	public HDD(){

	}

	public void run(){
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int[] nums = new int[n];
		int[] real = new int[n];
		for(int i = 0; i < n; i++){
			nums[i] = scan.nextInt();
		}
		int j = 0;
		for(int num: nums){
			real[num-1] = j;
			j++;
		}
		long total = 0;
		for(int i = 0; i < real.length-1; i++){
			total += Math.abs((real[i]- real[i+1]));
		}
		System.out.println(total);
		
	}

	public static void main(String[] args){
		HDD hdd = new HDD();
		hdd.run();
	}
}