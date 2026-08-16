import java.util.*;
import java.io.*;
public class cf{
    public static void main(String args[])throws Exception{
     Scanner sc=new Scanner(new BufferedReader(new InputStreamReader(System.in)));
	int n=sc.nextInt();
	ArrayList<String> ans=new ArrayList<>();
	HashMap<Long,Integer> indices=new HashMap<>();
	for(int i=0;i<n;i++){
	    long x=sc.nextLong();
	    if(!indices.containsKey(x))
		indices.put(x,i+1);
	    else{
		ans.add(""+indices.get(x)+" "+(i+1));
		indices=new HashMap<>();
	    }
	}
	if(ans.size()==0)System.out.println("-1");
	else{
	    int curr=1;
	    System.out.println(ans.size());
	    String y=ans.remove(ans.size()-1);
	    ans.add(y.substring(0,y.indexOf(' '))+" "+n);
	    for(String x:ans){
		System.out.println(""+curr+x.substring(x.indexOf(' ')));
		curr=Integer.parseInt(x.substring(x.indexOf(' ')+1))+1;
	    }
	}
    }
}
