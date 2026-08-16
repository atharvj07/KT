
import java.io.BufferedReader;

import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

import java.util.*;

public class Main {
	static class  ListaEncadeada 
	{
		private Nodo head;//ponteiro para o header da lista
		private Nodo tail;//ponteiro para o ultimo elemento da lista
		protected Nodo curr;//ponteiro paara o elemento atual da lista
		private int qnt;
		
		public int getQnt() {
			return qnt;
		}
		public Nodo getHead() {
			return head;
		}
		public void setHead(Nodo head) {
			this.head = head;
		}
		public Nodo getTail() {
			return tail;
		}
		public void setTail(Nodo tail) {
			this.tail = tail;
		}
		
		ListaEncadeada()
		{
			head=tail=curr= new Nodo(null);// header criado
			qnt=0;
		}
		public void clear()
		{
			head.setProximo(null);
			head=tail=curr= new Nodo(null);
			qnt=0;
			
		}
		public void inserir(Edge edge)//insere elemento na possicao atual (curr)
		{
			curr.setProximo(new Nodo(edge,curr.proximo()));
			if(tail==curr)
				tail = curr.proximo();
			qnt++;
		}
		public void append(Edge edge) //insere elemento no final da fila 
		{
			tail= tail.setProximo(new Nodo(edge,null));
			qnt++;
		}
		public Edge remove() 
		{
			if(curr.proximo()==null)//nada para remover
				return null;
			Edge removido = curr.proximo().getEdge(); //receptaculo de elemento removido a ser retornado
			
			if(tail == curr.proximo())//checa se o elemento removido eh o tail
				tail=curr;//atualiza o tail
			
			curr.setProximo(curr.proximo().proximo());
			qnt--;
			return removido;
			
		}
		public void moveToStart() 
		{
			curr=head;
		}
		public void moveToEnd() 
		{
			curr=tail;
		}
		public void next() 
		{
			if(curr!=tail)
			curr=curr.proximo();
		}
		public void prev()
		{
			Nodo busca = head;
			if(curr==head)//sem elemento anterior
				return;
			while(busca.proximo()!=curr)
			{
				busca = busca.proximo();
			}
			curr=busca;
		}
		public int lenght() 
		{
			return this.qnt;
		}
		public int currPos() 
		{
			Nodo busca=head;
			int x=0;
			while(busca!=tail)
			{
				busca=busca.proximo();
				x++;
			}
			return x;
		}
		public void moveToPos(int pos) 
		{
			Nodo busca = head;
			
			assert (pos>=0) && (pos<=qnt) : "Position out of range";
			for(int x=0;x<pos;x++)
			{
				busca=busca.proximo();
			}
			
		}
		public Edge getValue() 
		{
			if(curr==null)
				return null;
			if(curr.proximo()==null)
				return null;
			return curr.proximo().getEdge();
		}
		
	}

	static class Nodo
	{
		private Edge edge;
		private Nodo proximo;
		
		Nodo(Nodo proximo)
		{
			this.proximo=proximo;
		}
		Nodo(Edge elemento,Nodo next)
		{
			this.edge=elemento;
			this.proximo=next;
		}

		public Edge getEdge() {
			return edge;
		}

		public void setEdge(Edge edge) {
			this.edge = edge;
		}

		public Nodo proximo() {
			return proximo;
		}

		public Nodo setProximo(Nodo proximo) {
			this.proximo = proximo;
			return proximo;
		}
		
		
	}

	static class Edge 
	{
		private int vert;//, wt;
		public Edge(int v)//, int w) // Constructor
		{ vert = v;}// wt = w; }
		public int vertex() { return vert; }
		//public int weight() { return wt; }
	}

	static class Graphl 
	{
		
		private ListaEncadeada[] vertex; // The vertex list
		private int numEdge; // Number of edges
		private int[] Mark; // The mark array
		private int qntCiclos=0;
		
		public Graphl() {}
		
		
		public int getQntCiclos() {
			return qntCiclos;
		}

		public ListaEncadeada[] getVertex() {
			return vertex;
		}

		public void setVertex(ListaEncadeada[] vertex) {
			this.vertex = vertex;
		}

		public Graphl(int n) // Constructor
		{ Init(n); }
		
		
		public void Init(int n) 
		{
			Mark = new int[n];
			vertex = new ListaEncadeada[n];
			for (int i=0; i<n; i++)
				vertex[i] = new ListaEncadeada();
				
			numEdge = 0;
		}
		public int n() { return Mark.length; } // # of vertices
		public int e() { return numEdge; } // # of edges
		
		
		public int first(int v) 
		{
			if (vertex[v].getQnt() == 0)//size() == 0)
				return Mark.length; // No neighbor
			vertex[v].moveToStart();
			Edge it = vertex[v].getValue();
			return it.vertex();
		}
		/** @return v’s next neighbor after w*/ 
		public int next(int v, int w) 
		{
			Edge it = null;
			
			if (isEdge(v, w)) 
			{
				vertex[v].next();
				it = vertex[v].getValue();
			}
			if (it != null)
				return it.vertex();
			return Mark.length; // No neighbor
		}
		public boolean isEdge(int v, int w) 
		{
			Edge it = vertex[v].getValue();
			
			// Check if j is the current neighbor in the list
			if ((it != null) && (it.vertex() == w)) 
				return true;
			for (vertex[v].moveToStart();vertex[v].currPos() < vertex[v].getQnt();vertex[v].next()) // Check whole list
				if (vertex[v].getValue().vertex() == w)
					return true;
			return false;
		}
		
		/** Set the weight for an edge*/ 
		public void setEdge(int i, int j, int weight) 
		{
			assert weight != 0 : "May not set weight to 0";
			Edge currEdge = new Edge(j);//, weight);
			if (isEdge(i, j)) 
			{ // Edge already exists in graph
				vertex[i].remove();
				vertex[i].inserir(currEdge);
			}
			else 
			{ // Keep neighbors sorted by vertex index
				numEdge++;
				for (vertex[i].moveToStart();vertex[i].currPos() < vertex[i].getQnt();vertex[i].next())
					if (vertex[i].getValue().vertex() > j) 
						break;
				vertex[i].inserir(currEdge);
			}
		}
		/** Delete an edge */
		public void delEdge(int i, int j)
		{ 
			if (isEdge(i, j)) 
			{ 
				vertex[i].remove(); 
				numEdge--; 
			} 
		}
		
		/*public int weight(int i, int j) 
		{
			if (isEdge(i, j)) 
				return vertex[i].getValue().weight();
			return 0;
		}*/
		
		public void setMark(int v, int val) { Mark[v] = val; }
		public int getMark(int v) { return Mark[v]; }
		
		
		
		public void graphTraverseDFS() 
		{
			
			for (int v=0; v<n(); v++)
				setMark(v, 0);//UNVISITED); // Initialize
			for (int v=0; v<n(); v++)
				if (getMark(v) ==0)//== UNVISITED)
					//doTraverse(v);
					if(DFS(v))
						qntCiclos++;
		}
		/** Depth first search */
		public boolean DFS(int v) 
		{
			boolean resposta=true;
			 //preVisit(v); //o que quer que seja feito quando chegar no vertice
			 if(vertex[v].getQnt()==2)
			 { 
				 setMark( v, 1);//VISITED
				 int w = first(v);
				 while (w < n())
				 {
					 if (getMark(w) == 0)//==UNVISITED
							resposta=DFS( w) ;
					 w = next(v, w);
				 }
				 //posVisit( v);// o que quer que seja feito quando for sair do vertice"terminou de visitar"
				 if(resposta)
					 return true;
				 return false;
			 }
			 else
				 return false;
			 
		}
		public void graphTraverseBFS() 
		{
			
			for (int v=0; v<n(); v++)
				setMark(v, 0);//UNVISITED); // Initialize
			for (int v=0; v<n(); v++)
				if (getMark(v) ==0)//== UNVISITED);
					BFS(v);//doTraverse(v);
					
		}	
		public void BFS(int start)
		{
			//Queue<MyObject> queue = new LinkedList<MyObject>();
			Queue <Integer> Q = new LinkedList<Integer>();
			Q.add(start);
			setMark(start, 1);//VISITED);
			int v;
			int w;
			while (Q.size() > 0)
			{
				v= Q.remove();
				//preVisit(v);
				w = first( v);
				while( w < n() )
				{
					if (getMark(w) == 0 )//== UNVISITED )
					{
						setMark(w, 1);//VISITED);
						Q.add(w);
					}
					w = next(v, w);
				}
				//posVisit(g, v);
			}
		}
		
	}
	static class FastReader 
    { 
        BufferedReader br; 
        StringTokenizer st; 
  
        public FastReader() 
        { 
            br = new BufferedReader(new
                     InputStreamReader(System.in)); 
        } 
  
        String next() 
        { 
            while (st == null || !st.hasMoreElements()) 
            { 
                try
                { 
                    st = new StringTokenizer(br.readLine()); 
                } 
                catch (IOException  e) 
                { 
                    e.printStackTrace(); 
                } 
            } 
            return st.nextToken(); 
        } 
  
        int nextInt() 
        { 
            return Integer.parseInt(next()); 
        } 
  
        long nextLong() 
        { 
            return Long.parseLong(next()); 
        } 
  
        double nextDouble() 
        { 
            return Double.parseDouble(next()); 
        } 
  
        String nextLine() 
        { 
            String str = ""; 
            try
            { 
                str = br.readLine(); 
            } 
            catch (IOException e) 
            { 
                e.printStackTrace(); 
            } 
            return str; 
        } 
    }
	public static void main(String[] args) {
		FastReader scan = new FastReader();
		Graphl graph = new Graphl(scan.nextInt());
		int qntedges=scan.nextInt();
		for(int i =0, verticeSaida=0,verticeChegada=0;i<qntedges;i++)
		{
			verticeSaida=scan.nextInt()-1;
			verticeChegada=scan.nextInt()-1;
			graph.getVertex()[verticeSaida].append(new Edge(verticeChegada));
			graph.getVertex()[verticeChegada].append(new Edge(verticeSaida));
		}
		graph.graphTraverseDFS();
		System.out.println(graph.getQntCiclos());
	}

}

	 	 	 			   	 	 				 			 	  	