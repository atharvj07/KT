import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * @author: zhaoqing
 * @date: 2018/9/12
 * @time: 下午2:29
 */
public class Palindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int  n=sc.nextInt();
        int  a=sc.nextInt();
        int  b=sc.nextInt();
        int min=a>b?b:a;
        List<Integer> list=new ArrayList<>();
        for(int i=0;i<n;i++){
            list.add(sc.nextInt());
        }
        int result=0;
        int len=list.size();
        int helflen=list.size()/2;
        int mid=list.size()%2;
        for(int i=0;i<helflen;i++){
            if(list.get(i)!=2 && list.get(len-1-i)!=2){
                if(!list.get(i).equals(list.get(len - 1 - i))){
                    result=-1;
                    break;
                }
                if(list.get(i).equals(list.get(len - 1 - i))){
                    continue;
                }
            }
            if(list.get(i)==2 && list.get(len-1-i)==2){
                result=result+2*min;
                continue;
            }
            if(list.get(i)==2){
                if(list.get(len-1-i)==1){
                    result=result+b;
                }else {
                    result=result+a;
                }
            }
            if(list.get(len-1-i)==2){
                if(list.get(i)==1){
                    result=result+b;
                }else {
                    result=result+a;
                }
            }

        }
        if(result==-1){
            System.out.println(-1);
        }else {
            if(mid==1){
                if(list.get(helflen)==2){
                    result=result+min;
                }
            }
            System.out.println(result);
        }
    }
}
