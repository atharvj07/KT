class Main{
public static void main(String[]args){
int a=new java.util.Scanner(System.in).nextInt();
  for(int i=1;i<=360;i++){
  if((a*i)%360==0){System.out.println(i);break;}
  }
}
}
