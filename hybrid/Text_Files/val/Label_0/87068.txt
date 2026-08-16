import java.io.*;
import java.util.*;
import java.lang.*;

class Main{
  public static void main(String[] args) throws IOException{
    Scanner scan=new Scanner(System.in);
    int n=Integer.parseInt(scan.next());
    int q=Integer.parseInt(scan.next());
    int sumTime=0;
    Queue<Process> queue=new ArrayDeque<Process>();

    for(int i=0;i<n;i++){
      String namae=scan.next();
      int Time=Integer.parseInt(scan.next());
      queue.add(new Process(namae,Time));
    }

    Queue<Process> ans=new ArrayDeque<>();
    while(!queue.isEmpty()){
      Process buf=queue.remove();
      if(buf.pTime-q<=0){
        int buf2=buf.pTime;
        buf.pTime+=sumTime;
        sumTime+=buf2;
        ans.add(buf);
      }else {
        buf.pTime-=q;
        queue.add(buf);
        sumTime+=q;
      }
    }
    for(Process p:ans){
      System.out.println(p.name+" "+p.pTime);
    }
  }
}
class Process{
  String name;
  int pTime;

  public Process(String name,int pTime){
    this.name=name;
    this.pTime=pTime;
  }
}

