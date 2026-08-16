

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class TheTextSplitting_CodeForces {

	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String temp [] = br.readLine().split(" "); 
		int n = Integer.parseInt(temp[0]);
		int p = Integer.parseInt(temp[1]);
		int q = Integer.parseInt(temp[2]);
		String s =br.readLine();
	//	System.out.println(50/3);
		//System.out.println(40/14);
		if(p+q==n){
			System.out.println(2);
			System.out.println(s.substring(0,p));
			System.out.println(s.substring(p));
			System.exit(0);
		}
		if(n%p==0){
			int parts = n/p;
			int start=0;
			System.out.println(parts);
			for(int i=0;i<parts;i++){
				System.out.println(s.substring(start,start+p));
				start+=p;
			}
			System.exit(0);
		}
		
		if(n%q==0){
			int parts = n/q;
			int start=0;
			System.out.println(parts);
			for(int i=0;i<parts;i++){
				System.out.println(s.substring(start,start+q));
				start+=q;
			}
			System.exit(0);
		}
		int max =Math.max(p,q);
		int min = Math.min(p, q);
		int te=n;
		int maxNum=0;
		int minNum=0;
		while(te>=0){
			te-=max;
			maxNum++;
			if(te%min==0){
				minNum=te/min;
				break;
			}
		}
		if(minNum>0){
			//System.out.println("hereee "+ minNum);
			System.out.println(minNum+maxNum);
			int begin=0;
			for(int i=0;i<maxNum;i++){
				System.out.println(s.substring(begin, begin+max));
				begin+=max;
			}
			for(int i=0;i<minNum;i++){
				System.out.println(s.substring(begin, begin+min));
				begin+=min;
			}
			
			System.exit(0);
		}
		
		int rem = n%max;
		int maxTimes=0;
		int minTimes=0;
		if(rem%min==0){
			maxTimes=n/max;
			minTimes = rem/min;
		
		System.out.println(maxTimes+minTimes);
		int begin=0;
		for(int i=0;i<maxTimes;i++){
			System.out.println(s.substring(begin,begin+max));
			begin+=max;
		}
		//begin=0;
		for(int i=0;i<minTimes;i++){
			System.out.println(s.substring(begin,begin+min));
			begin+=min;
		}
		System.exit(0);
		}
		else 
		{
			System.out.println(-1);
			System.exit(0);
		}
			
//		if(n%p!=0 && n%q!=0){
//			System.out.println(-1);
//			System.exit(0);
//		}
		
		

	}
}
