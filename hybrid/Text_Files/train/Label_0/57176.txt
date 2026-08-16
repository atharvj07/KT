import java.io.*;
import java.util.*;

public class Main{
    
    public static void main(String agrs[]) throws IOException{
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

	while(true){
	    int n=Integer.parseInt(br.readLine());

	    if(n==0)
		break;

	    ArrayList<String> list=new ArrayList<>();

	    int max=0;

	    for(int i=0;i<n;i++){
		String str[]=br.readLine().split("");

		StringBuilder sb=new StringBuilder(str[0]);
		for(int j=0;j<str.length;j++){
		    if((str[j].equals("a")||str[j].equals("e")||str[j].equals("i")||str[j].equals("o")||str[j].equals("u"))&&j!=str.length-1){
		        sb.append(str[j+1]);
		    }
		}
		list.add(sb.toString());
		//System.out.println(sb.toString());
		max=Math.max(max,sb.toString().length());
	    }

	    HashSet<String> set=new HashSet<>();
	    int k=1;
	    boolean flag=false;

	    for(;k<=max;k++){
		flag=false;
		
		for(int i=0;i<list.size();i++){
		    String s= (list.get(i).length()<k) ? list.get(i) : list.get(i).substring(0,k);

		    if(set.contains(s)){
			flag=true;
			break;
		    }
		    set.add(s);
		}

		if(!flag){
		    break;
		}
		set.clear();
	    }

	    if(flag)
		System.out.println("-1");
	    else
		System.out.println(k);
	}
    }
}
    

