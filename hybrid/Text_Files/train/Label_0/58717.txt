import java.io.*;
import java.util.*;
import java.math.*;
class Main{
    public static void main(String[] args){
	BufferedReader sc=new BufferedReader(new InputStreamReader(System.in));
	try {
	    while(true){
		long z = Integer.valueOf(sc.readLine());
		if(z==0)
		    break;
		long mulz = z*z*z;
		long max = 0;
		for(long i=1; i<z; i++)
		    for(long j=1; j<z; j++){
			long tmp = i*i*i+j*j*j;
			if(tmp<mulz)
			    max = Math.max(max,tmp);
		    }
		System.out.println(mulz-max);
	    }
	}catch(Exception e){
	    System.out.println("Error");
	}
    }
}