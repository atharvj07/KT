import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args){
	try{
	    BufferedReader sc=new BufferedReader(new InputStreamReader(System.in));
	    int i, n = Integer.valueOf(sc.readLine());
	    int[] map = new int[n];
	    String[] st = sc.readLine().split(" ");
	    for(i=0; i<n; i++)
		map[i] = Integer.valueOf(st[i]);
	    Arrays.sort(map);
	    long sum = 0;
	    for(i=0; i<=n; i++){
		if(i==n||map[i]>sum+1){
		    System.out.println(sum+1);
		    break;
		}
		sum += map[i];
	    }
	}catch(Exception e){
	    System.out.println("Error");
	}
    }
}