import java.awt.geom.Line2D;
import java.awt.geom.Point2D;
import java.awt.geom.Point2D.Double;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.TreeSet;
import java.lang.Object;
 
public class Main {
    Scanner sc = new Scanner(System.in);
   
    public static void main(String[] args) {
        new Main(); 
    }
   
    public Main() {
        new aoj1232().doIt();
    }
    class aoj1232{
    	ArrayList<Integer> prime = new ArrayList<Integer>();
    	void eratos(){ int MAX = 1000000;
    		boolean [] isprime = new boolean[MAX + 1];
    		Arrays.fill(isprime, true);
    		isprime[0] = false;
    		isprime[1] = false;
    		for(int i = 0; i * i <= MAX; i++){
    			if(isprime[i]){
    				for(int j = i * 2; j <= MAX; j+= i){
    					isprime[j] = false;
    				}
    			}
    		}
    		for(int i = 0; i <= 10000; i++){
    			if(isprime[i])prime.add(i);
    		}
    	}
    	void doIt(){
    		eratos();
    		while(true){
    			double n = sc.nextDouble();
    			double a = sc.nextDouble();
    			double b = sc.nextDouble();
    			if(n+a+b == 0)break;
    			double sum = a/b;
    			double max = 0;
    			int numa = 0,numb = 0;
    			for(int i = 0;i < prime.size();i++){
    				for(int j = i;j < prime.size();j++){
    					double num = prime.get(i)*1.0/prime.get(j);
    					if(num < sum || prime.get(i)*prime.get(j) > n)break;
    					if(max < prime.get(i)*prime.get(j)){
    						max = prime.get(i)*prime.get(j);
    						numa = prime.get(i);
    						numb = prime.get(j);
    					}
    				}
    			}
    			System.out.println(numa+" "+numb);
    		}
    	}
    }
}