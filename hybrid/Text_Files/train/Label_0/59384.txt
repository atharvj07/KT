import java.io.*;
import java.util.*;

public class C
{
	String line;
	StringTokenizer inputParser;
	BufferedReader is;
	FileInputStream fstream;
	DataInputStream in;
	
	void openInput(String file)
	{

		if(file==null)is = new BufferedReader(new InputStreamReader(System.in));//stdin
		else
		{
			try{
		
				
			fstream = new FileInputStream(file);
			in = new DataInputStream(fstream);
			is = new BufferedReader(new InputStreamReader(in));
			}catch(Exception e)
			{
				System.err.println(e);
			}
		}

	}
	
	void readNextLine()
	{
		try {
			line = is.readLine();
			inputParser = new StringTokenizer(line, " ");
			//System.err.println("Input: " + line);
		} catch (IOException e) {
			System.err.println("Unexpected IO ERROR: " + e);
		}	
		
	}
	
	int NextInt()
	{
		String n = inputParser.nextToken();
		int val = Integer.parseInt(n);
		
		//System.out.println("I read this number: " + val);
		return val;
	}
	
	String NextString()
	{
		String n = inputParser.nextToken();
		return n;
	}
	
	void closeInput()
	{
		try {
			is.close();
		} catch (IOException e) {
			System.err.println("Unexpected IO ERROR: " + e);
		}
			
	}
	
	
	public static void main(String [] argv)
	{
		String filePath=null;
		if(argv.length>0)filePath=argv[0];
		C c = new C(filePath);
	}
	long [] f = new long[70];
	
	public C(String inputFile)
	{
		long ret=0;
		openInput(inputFile);
		
		readNextLine();
		int N=line.length();
		ArrayList <Worker> list = new ArrayList <Worker>();
		
		
		f[0]=1;
		for(int i=1; i<70; i++)f[i]=i*f[i-1];
		//System.out.println(f[69]);
			
		String n="";
		Worker up=null;
		String el=":.,";
		for(int i=0; i<N; i++)
		{
			if(el.indexOf(line.charAt(i))>-1)
			{
				if(n.length()>0)
				{
					Worker w=new Worker (n, up);
				
					list.add(w);
					up=w;
					n="";
				}
				
				switch(line.charAt(i))
				{
					case ':':
						break;
					case '.':
						up=up.up;
						break;
					case ',':
						break;
				}
				
			}
			else n+=line.charAt(i);
		
		}
		
		for(int i=0; i<list.size(); i++)
		{
			//long nn=list.get(i).getNum(list.get(i).name);
			//System.out.println(list.get(i).name+" "+nn);
			ret+=list.get(i).getNum(list.get(i).name);
		}
		//ret/=2;
		
		System.out.println(ret);
		
        
        closeInput();
	}

	class Worker
	{
		Worker up;
		ArrayList <Worker> down;
		String name;
		long myNum=-1;
		
		
		Worker(String n, Worker chef)
		{
			up=chef;
			name=n;
			down = new ArrayList<Worker>();
			if(chef!=null)chef.addSub(this);
		}
		
		void addSub(Worker w)
		{
			down.add(w);
		}
		
		long getNum(String s)
		{
			//if(myNum>-1)return myNum;
			long ret=0;
			for(int i=0; i<down.size(); i++)
			{
				if(down.get(i).name.compareTo(s)==0)
				{
					ret++;
					
				}
				ret+=down.get(i).getNum(s);
			}
			myNum=ret;
			return ret;
		}
	}

	
}

