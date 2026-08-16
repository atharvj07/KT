/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import static java.lang.Math.abs;
import static java.lang.Math.sqrt;
import java.util.Scanner;


/**
 *
 * @author ANDRES
 */
public class AAAA {  //Convex husk->Suplementary triangle
    
    static int cont;
    Scanner sc;
    int n;
    long s;
    long px[];
    long py[];
    int bax,bay,bbx,bby,bcx,bcy;
    double maxArea;
    int a,b,c;
    
    
    AAAA(){
        sc = new Scanner(System.in);
        
        n = sc.nextInt();
        s = sc.nextLong();
        
        px = new long[n];
        py = new long[n];

        cont = 1;
        
        for(int i =0;i<n;i++){
            
            px[i] = sc.nextInt();
            py[i] = sc.nextInt();
        }
        
        a = 0;
        b = 1;
        c = 2;
        
        int flag = 0;
        
        while(true){ 

            flag = 0; 
            for(int i = 0;i<n;i++){
                if(Area(px[i],py[i],px[b],py[b],px[c],py[c])>Area(px[a],py[a],px[b],py[b],px[c],py[c])){
                    a = i;
                    flag =1;
                }
                if(Area(px[a],py[a],px[i],py[i],px[c],py[c])>Area(px[a],py[a],px[b],py[b],px[c],py[c])){
                    b = i;
                    flag = 1;
                }
                if(Area(px[a],py[a],px[b],py[b],px[i],py[i])>Area(px[a],py[a],px[b],py[b],px[c],py[c])){
                    c = i;
                    flag =1;
                }
                
            }
            if(flag == 0){
                break;
            }

        }
            
        System.out.println(((px[c]-px[a])+px[b])+" "+((py[b]-py[a])+py[c]));
        System.out.println(((px[a]-px[c])+px[b])+" "+((py[b]-py[c])+py[a]));
        System.out.println(((px[c]-px[b])+px[a])+" "+((py[c]-py[b])+py[a]));

        
        

    }
    
    
    double Area(long ax,long ay,long bx,long by, long cx,long cy){ //100%funcional
       
        long A;
        long B;
        double lad1,lad2,lad3,semp,area;
        
        A = abs(ax - bx);
        B = abs(ay - by);
        lad1 = (sqrt((double)(A*A)+(double)(B*B)));
        
        A = abs(ax - cx);
        B = abs(ay - cy);
        
        lad2 = (sqrt((double)(A*A)+(double)(B*B)));
        
        A = abs(bx - cx);
        B = abs(by - cy);
        
        lad3 = (sqrt((double)(A*A)+(double)(B*B)));
        
        semp = (lad1+lad2+lad3)/2;
        
        area = sqrt(semp*(semp-lad1)*(semp-lad2)*(semp-lad3));
        
        
        return area;
        
    }
    
    public static void main(String args[]){
        AAAA a = new AAAA();
        
        
    }
}
