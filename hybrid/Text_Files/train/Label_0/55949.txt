import java.util.*;

class Main{
	public static void main(String[]args){
    	Scanner scan = new Scanner(System.in);
      	int x = scan.nextInt();
      	boolean found = false;
      	while(true){
          for(int i=x;;i++){
            int y=2;
            for(;y<Math.sqrt(i);y++){
            	if(i%y==0)break;
            }
            if(Math.sqrt(i)<y)
            found=true;
            if(found){
                  System.out.println(i);
              return;
            }  
          }
        
        }
    }
}