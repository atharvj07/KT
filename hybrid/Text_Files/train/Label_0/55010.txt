import java.util.*;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        char[] c = sc.next().toCharArray();
        Arrays.sort(c);
        int count =1;
        boolean ans = true;
        for(int i =1;i<c.length;i++){
            if(c[i-1]!=c[i]){
                if(count%2!=0){
                    ans = false;
                    break;
                }
            }
            count ++;
        }
        if(count%2!=0){
            ans = false;
        }
        if(ans){
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}