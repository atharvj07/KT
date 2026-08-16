import java.util.*;

public class Main {
    
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        s.nextLine();
        String str = s.nextLine();
        boolean flag = true;
        for(int i = 0;i<n && n!=1;i++){
            if(str.charAt(i)=='0'){
                if(i==0){
                    if(str.charAt(1)=='0'){
                        flag = false;
                        break;
                    }
                }else if(i==n-1){
                    if(str.charAt(n-2)=='0'){
                        flag=false;
                        break;
                    }
                }else{
                    if(str.charAt(i-1)=='0' && str.charAt(i+1)=='0'){
                        flag=false;
                        break;
                    }
                }
            }else{
                if(i==0){
                    if(str.charAt(1)=='1'){
                        flag = false;
                        break;
                    }
                }else if(i==n-1){
                    if(str.charAt(n-2)=='1'){
                        flag=false;
                        break;
                    }
                }else{
                    if(str.charAt(i-1)=='1' || str.charAt(i+1)=='1'){
                        flag=false;
                        break;
                    }
                }
            }
        }
        if(n==1 && str.equals("0")) flag = false;
        if(flag){
            System.out.println("Yes");
        }else System.out.println("No");
    }

}