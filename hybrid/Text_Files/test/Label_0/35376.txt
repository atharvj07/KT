import java.io.*;
import java.util.*;

public class game{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        for(int i = 0; i<t; i++){
            String s =scan.next();
            int count1 = 0;
            int count0 = 0;
            int count = 0;
            for(int j = 0; j<s.length(); j++){
                if(s.charAt(j) == '0'){
                    count0++;
                }
                if(s.charAt(j) == '1'){
                    count1++;
                }
            }
            if(count1>count0){
                count = count0;
            }else{
                count = count1;
            }
            
            // for(int j = 1; j<s.length(); j++){
            //     if(s.charAt(j) == '1' && s.charAt(j-1) == '0'){
            //         count++;
            //     }
            //     if(s.charAt(j) == '0' && s.charAt(j-1) == '1'){
            //         count++;
            //     }
            //     if(j>2){
            //         if(s.charAt(j) == '1' && s.charAt(j-3) == '0'){
            //             if(s.charAt(j-1) == '1' && s.charAt(j-2) == '0'){
            //                 count++;
            //             }
        
            //         }
            //         if(s.charAt(j) == '0' && s.charAt(j-3) == '1'){
            //             if(s.charAt(j-1) == '0' && s.charAt(j-2) == '1'){
            //                 count++;
            //           }
            //         }
            //     }
            //     if(j>2){
            //         if(s.charAt(j) == '0' && s.charAt(j-1) == '0' && s.charAt(j-2) == '1' && s.charAt(j-3) == '0'){
            //             count--;
            //         }
            //         if(s.charAt(j) == '1' && s.charAt(j-1) == '0' && s.charAt(j-2) == '1' && s.charAt(j-3) == '1'){
            //             count--;
            //         }
            //     }
            // }
            if(count%2 == 0){
                System.out.println("NET");
            }else{
                System.out.println("DA");
            }
        }
    }
}                
           














