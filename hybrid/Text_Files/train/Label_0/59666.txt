import java.util.Scanner;
public class freebie{
public static void main(String[] args){
int n,c;
Scanner sc = new Scanner(System.in);
n=sc.nextInt();
c=sc.nextInt();
int[] array = new int[n+1];
array[n] = 0 ;
for(int i = 0;i<n;i++){
array[i]=sc.nextInt();}
int [] difference = new int[n];
int temp = 0 ;
for(int i=0;i<(n-1);i++){
difference[i] = array[i] - array[i+1] -c;
if(temp<difference[i])
temp = difference[i];}
System.out.println(temp);
}}