import java.util.*;

public class Main{
	private static Scanner sc=new Scanner(System.in);
	
	public static void main(String[] args){
		String s=sc.next();
        int k=readInt();
        Set<String> set=new TreeSet<>();
        int l=s.length();
        for(int t=0;t<26;t++){
            if(set.size()>=k)break;
            for(int i=0;i<l;i++){
                if('a'+t==s.charAt(i)){
                    for(int j=i+1;j<=l&&j-i<=k;j++)
                        set.add(s.substring(i,j));
                }
            }
        }
        int i=1;
        for(String t:set){
            if(i==k){
                System.out.println(t);
                break;
            }
            i++;
        }
	}
	
	private static int readInt(){
		return Integer.parseInt(sc.next());
	}
	private static long readLong(){
		return Long.parseLong(sc.next());
	}
}