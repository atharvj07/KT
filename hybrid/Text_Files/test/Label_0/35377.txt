import java.util.*;
import java.io.*;
public class Bathroom{
    static char replace[]={'a','b','c','d','e','#'};
    static HashMap<String,Integer> hs=new HashMap<>();
    public static int solveOne(String str,ArrayList<Integer> pts){
        char[] arr=str.toCharArray();
        int ans=0;
        int a=pts.get(0);
        for(int i=0;i<replace.length;i++){
            arr[a]=replace[i];
            StringBuilder s=new StringBuilder();
            for(Character ch:arr)
              if(ch!='#') s.append(ch);
            if(hs.containsKey(s.toString())) ans+=hs.get(s.toString());
        }
        return ans;
    }
    public static int solveTwo(String str,ArrayList<Integer> pts){
        int a=pts.get(0),b=pts.get(1);
        HashSet<String> done=new HashSet<>();
        int ans=0;
        char arr[]=str.toCharArray();
        for(int i=0;i<replace.length;i++){
            arr[a]=replace[i];
            for(int j=0;j<replace.length;j++){
                arr[b]=replace[j];
                StringBuilder s=new StringBuilder();
                for(Character ch:arr)
                    if(ch!='#') s.append(ch);
                if(done.contains(s.toString())) continue;
                if(hs.containsKey(s.toString())) ans+=hs.get(s.toString());
                done.add(s.toString());
            }
        }
        return ans;
    }
    public static int solveZero(String s){
        int ans=0;
        if(hs.containsKey(s)) return hs.get(s);
        else return 0;
    }
    public static int solveThree(String str,ArrayList<Integer> pts){
        int a=pts.get(0),b=pts.get(1),c=pts.get(2);
        HashSet<String> done=new HashSet<>();
        int ans=0;
        char arr[]=str.toCharArray();
        for(int i=0;i<replace.length;i++){
            arr[a]=replace[i];
            for(int j=0;j<replace.length;j++){
                arr[b]=replace[j];
                for(int k=0;k<replace.length;k++){
                    arr[c]=replace[k];
                    StringBuilder s=new StringBuilder();
                    for(Character ch:arr)
                        if(ch!='#') s.append(ch);
                    if(done.contains(s.toString())) continue;
                    if(hs.containsKey(s.toString())) ans+=hs.get(s.toString());
                    done.add(s.toString());
                }
            }
        }
        return ans;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int q=sc.nextInt();
        for(int i=0;i<n;i++){
            String s=sc.next();
            if(hs.containsKey(s))
              hs.put(s,hs.get(s)+1);
            else
              hs.put(s,1);
        }
        while(q-->0){
            String s=sc.next();
            ArrayList<Integer> pts=new ArrayList<>();
            for(int i=0;i<s.length();i++)
              if(s.charAt(i)=='?')
               pts.add(i);
            
            if(pts.size()==1) System.out.println(solveOne(s,pts)); 
            else if(pts.size()==2) System.out.println(solveTwo(s,pts)); 
            else if(pts.size()==3) System.out.println(solveThree(s,pts));
            else if(pts.size()==0) System.out.println(solveZero(s)); 
        }
    }
}