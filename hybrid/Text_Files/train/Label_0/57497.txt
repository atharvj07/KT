import java.util.*;
public class Main {
public static void main(String [] args){
	Scanner in=new Scanner(System.in);
	int n=in.nextInt();
	int k=in.nextInt();
	int array[]=new int[n];
    	for(int i=0;i<n;i++)array[i]=in.nextInt();
    	int leftPtr=0;
    	int rightPtr=0;
              	HashMap<Integer,Integer>map=new HashMap<Integer,Integer>();
              	long ans=0;
              	boolean move=true;
	while(leftPtr < n && move){
	Integer a=map.get(array[rightPtr]);
    long addVal=n-rightPtr;
    int temp=1;
	if(a==null)	
	map.put(array[rightPtr],1);
	else {
	map.put(array[rightPtr],a+1);temp=a+1;
	}
 	              if(temp>=k){
	                boolean flag=true;
	                long prev=leftPtr;
	                while(flag){
	                Integer x=map.get(array[leftPtr]);
	                map.put(array[leftPtr],x-1);leftPtr++;
	                if(x==k){
	                flag=false;ans+=(leftPtr-prev)*addVal;
    }
    //System.out.println(leftPtr+" "+rightPtr+" "+ans);
}
}
rightPtr++;
if(rightPtr==n)move=false;
//System.out.println("1"+" "+rightPtr+" "+addVal+" "+temp+" "+move);
}
System.out.print(ans);
}
}