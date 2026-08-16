import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.math.BigInteger;
import java.util.AbstractMap;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Comparator;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.NoSuchElementException;
import java.util.Set;
import java.util.SortedMap;
import java.util.SortedSet;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.function.BiConsumer;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Supplier;
import java.util.stream.Stream;

public class E_418
{
	public static final long[] POWER2 = generatePOWER2();
	public static final BigInteger[] FACULTY_BIG = generateFacultyBig();
	public static final BigInteger TWO = BigInteger.valueOf(2);
	public static final long BIG = 1000000007;
	public static final IteratorBuffer<Long> ITERATOR_BUFFER_PRIME = new IteratorBuffer<>(streamPrime(1000000).iterator());
	private static BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
	private static StringTokenizer stringTokenizer = null;
	private static PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));

	interface BiFunctionResult<Type0, Type1, TypeResult>
	{
		TypeResult apply(Type0 x0, Type1 x1, TypeResult x2);
	}

	static class Array<Type> implements Iterable<Type>
	{
		private Object[] array;

		public Array(int size)
		{
			this.array = new Object[size];
		}

		public Array(int size, Type element)
		{
			this(size);
			Arrays.fill(this.array, element);
		}

		public Array(Array<Type> array, Type element)
		{
			this(array.size() + 1);
			for (int index = 0; index < array.size(); index++)
			{
				set(index, array.get(index));
			}
			set(size() - 1, element);
		}

		public Array(List<Type> list)
		{
			this(list.size());
			int index = 0;
			for (Type element : list)
			{
				set(index, element);
				index += 1;
			}
		}

		public Type get(int index)
		{
			return (Type) this.array[index];
		}

		public Array set(int index, Type value)
		{
			this.array[index] = value;
			return this;
		}

		public int size()
		{
			return this.array.length;
		}

		public List<Type> toList()
		{
			List<Type> result = new ArrayList<>();
			for (Type element : this)
			{
				result.add(element);
			}
			return result;
		}

		@Override
		public Iterator<Type> iterator()
		{
			return new Iterator<Type>()
			{
				int index = 0;

				@Override
				public boolean hasNext()
				{
					return this.index < size();
				}

				@Override
				public Type next()
				{
					Type result = Array.this.get(index);
					index += 1;
					return result;
				}
			};
		}

		@Override
		public String toString()
		{
			return "[" + E_418.toString(this, ", ") + "]";
		}
	}

	static abstract class Edge<TypeVertex extends Vertex<TypeVertex, TypeEdge>, TypeEdge extends Edge<TypeVertex, TypeEdge>>
	{
		public final TypeVertex vertex0;
		public final TypeVertex vertex1;
		public final boolean bidirectional;

		public Edge(TypeVertex vertex0, TypeVertex vertex1, boolean bidirectional)
		{
			this.vertex0 = vertex0;
			this.vertex1 = vertex1;
			this.bidirectional = bidirectional;
			this.vertex0.edges.add(getThis());
			if (this.bidirectional)
			{
				this.vertex1.edges.add(getThis());
			}
		}

		public TypeVertex other(Vertex<TypeVertex, TypeEdge> vertex)
		{
			TypeVertex result;
			if (vertex0 == vertex)
			{
				result = vertex1;
			}
			else
			{
				result = vertex0;
			}
			return result;
		}

		public abstract TypeEdge getThis();

		public void remove()
		{
			this.vertex0.edges.remove(getThis());
			if (this.bidirectional)
			{
				this.vertex1.edges.remove(getThis());
			}
		}

		@Override
		public String toString()
		{
			return this.vertex0 + "->" + this.vertex1;
		}
	}

	public static class EdgeDefault<TypeVertex extends Vertex<TypeVertex, EdgeDefault<TypeVertex>>> extends Edge<TypeVertex, EdgeDefault<TypeVertex>>
	{
		public EdgeDefault(TypeVertex vertex0, TypeVertex vertex1, boolean bidirectional)
		{
			super(vertex0, vertex1, bidirectional);
		}

		@Override
		public EdgeDefault<TypeVertex> getThis()
		{
			return this;
		}
	}

	public static class Vertex<TypeVertex extends Vertex<TypeVertex, TypeEdge>, TypeEdge extends Edge<TypeVertex, TypeEdge>> implements Comparable<Vertex<? super TypeVertex, ? super TypeEdge>>
	{
		public static <TypeVertex extends Vertex<TypeVertex, TypeEdge>, TypeEdge extends Edge<TypeVertex, TypeEdge>> void depthFirstSearch(
				Array<TypeVertex> vertices,
				int indexVertexStart,
				BiConsumer<TypeVertex, TypeEdge> functionPreVisit,
				BiConsumer<TypeVertex, TypeEdge> functionInVisit,
				BiConsumer<TypeVertex, TypeEdge> functionPostVisit
		)
		{
			TypeVertex vertexTo;
			TypeEdge edgeTo;
			boolean[] isOnStack = new boolean[vertices.size()];
			Stack<Operation> stackOperations = new Stack<>();
			Stack<TypeVertex> stackVertices = new Stack<>();
			Stack<TypeEdge> stackEdges = new Stack<>();

			TypeVertex vertexStart = vertices.get(indexVertexStart);
			stackOperations.push(Operation.EXPAND);
			stackVertices.push(vertexStart);
			stackEdges.push(null);
			isOnStack[vertexStart.index] = true;
			while (!stackOperations.isEmpty())
			{
				Operation operation = stackOperations.pop();
				TypeVertex vertex = stackVertices.pop();
				TypeEdge edge = stackEdges.pop();
				switch (operation)
				{
					case INVISIT:
						functionInVisit.accept(vertex, edge);
						break;
					case POSTVISIT:
						functionPostVisit.accept(vertex, edge);
						break;
					case EXPAND:
						stackOperations.push(Operation.POSTVISIT);
						stackVertices.push(vertex);
						stackEdges.push(edge);
						Integer indexTo = null;
						for (int index = 0; indexTo == null && index < vertex.edges.size(); index++)
						{
							edgeTo = vertex.edges.get(index);
							vertexTo = edgeTo.other(vertex);
							if (!isOnStack[vertexTo.index])
							{
								indexTo = index;
							}
						}
						if (indexTo != null)
						{
							edgeTo = vertex.edges.get(indexTo);
							vertexTo = edgeTo.other(vertex);
							stackOperations.push(Operation.EXPAND);
							stackVertices.push(vertexTo);
							stackEdges.push(edgeTo);
							isOnStack[vertexTo.index] = true;
							for (int index = indexTo + 1; index < vertex.edges.size(); index++)
							{
								edgeTo = vertex.edges.get(index);
								vertexTo = edgeTo.other(vertex);
								if (!isOnStack[vertexTo.index])
								{
									stackOperations.push(Operation.INVISIT);
									stackVertices.push(vertex);
									stackEdges.push(edge);
									stackOperations.push(Operation.EXPAND);
									stackVertices.push(vertexTo);
									stackEdges.push(edgeTo);
									isOnStack[vertexTo.index] = true;
								}
							}
						}
						functionPreVisit.accept(vertex, edge);
						break;
				}
			}
		}

		public static <TypeVertex extends Vertex<TypeVertex, TypeEdge>, TypeEdge extends Edge<TypeVertex, TypeEdge>> void depthFirstSearch(
				Array<TypeVertex> vertices,
				int indexVertexStart,
				Consumer<TypeVertex> functionPreVisit,
				Consumer<TypeVertex> functionInVisit,
				Consumer<TypeVertex> functionPostVisit
		)
		{
			depthFirstSearch(
					vertices,
					indexVertexStart,
					(vertex, edge) -> functionPreVisit.accept(vertex),
					(vertex, edge) -> functionInVisit.accept(vertex),
					(vertex, edge) -> functionPostVisit.accept(vertex)
			);
		}

		public static <TypeVertex extends Vertex<TypeVertex, TypeEdge>, TypeEdge extends Edge<TypeVertex, TypeEdge>, TypeResult> TypeResult breadthFirstSearch(
				TypeVertex vertex,
				TypeEdge edge,
				BiFunctionResult<TypeVertex, TypeEdge, TypeResult> function,
				Array<Boolean> visited,
				FIFO<TypeVertex> verticesNext,
				FIFO<TypeEdge> edgesNext,
				TypeResult result
		)
		{
			if (!visited.get(vertex.index))
			{
				visited.set(vertex.index, true);
				result = function.apply(vertex, edge, result);
				for (TypeEdge edgeNext : vertex.edges)
				{
					TypeVertex vertexNext = edgeNext.other(vertex);
					if (!visited.get(vertexNext.index))
					{
						verticesNext.push(vertexNext);
						edgesNext.push(edgeNext);
					}
				}
			}
			return result;
		}

		public static <TypeVertex extends Vertex<TypeVertex, TypeEdge>, TypeEdge extends Edge<TypeVertex, TypeEdge>, TypeResult> TypeResult breadthFirstSearch(
				Array<TypeVertex> vertices,
				int indexVertexStart,
				BiFunctionResult<TypeVertex, TypeEdge, TypeResult> function,
				TypeResult result
		)
		{
			Array<Boolean> visited = new Array<>(vertices.size(), false);
			FIFO<TypeVertex> verticesNext = new FIFO<>();
			verticesNext.push(vertices.get(indexVertexStart));
			FIFO<TypeEdge> edgesNext = new FIFO<>();
			edgesNext.push(null);
			while (!verticesNext.isEmpty())
			{
				result = breadthFirstSearch(verticesNext.pop(), edgesNext.pop(), function, visited, verticesNext, edgesNext, result);
			}
			return result;
		}

		public final int index;
		public final List<TypeEdge> edges;

		public Vertex(int index)
		{
			this.index = index;
			this.edges = new ArrayList<>();
		}

		@Override
		public int compareTo(Vertex<? super TypeVertex, ? super TypeEdge> that)
		{
			return Integer.compare(this.index, that.index);
		}

		@Override
		public String toString()
		{
			return "" + this.index;
		}

		enum Operation
		{
			INVISIT, POSTVISIT, EXPAND
		}
	}

	public static class VertexDefault<TypeEdge extends Edge<VertexDefault<TypeEdge>, TypeEdge>> extends Vertex<VertexDefault<TypeEdge>, TypeEdge>
	{
		public VertexDefault(int index)
		{
			super(index);
		}
	}

	public static class VertexDefaultDefault extends Vertex<VertexDefaultDefault, EdgeDefaultDefault>
	{
		public static Array<VertexDefaultDefault> vertices(int n)
		{
			Array<VertexDefaultDefault> result = new Array<>(n);
			for (int index = 0; index < n; index++)
			{
				result.set(index, new VertexDefaultDefault(index));
			}
			return result;
		}

		public VertexDefaultDefault(int index)
		{
			super(index);
		}
	}

	public static class EdgeDefaultDefault extends Edge<VertexDefaultDefault, EdgeDefaultDefault>
	{
		public EdgeDefaultDefault(VertexDefaultDefault vertex0, VertexDefaultDefault vertex1, boolean bidirectional)
		{
			super(vertex0, vertex1, bidirectional);
		}

		@Override
		public EdgeDefaultDefault getThis()
		{
			return this;
		}
	}

	public static class Tuple2<Type0, Type1>
	{
		public final Type0 v0;
		public final Type1 v1;

		public Tuple2(Type0 v0, Type1 v1)
		{
			this.v0 = v0;
			this.v1 = v1;
		}

		@Override
		public String toString()
		{
			return "(" + this.v0 + ", " + this.v1 + ")";
		}
	}

	static class Wrapper<Type>
	{
		public Type value;

		public Wrapper(Type value)
		{
			this.value = value;
		}

		public Type get()
		{
			return this.value;
		}

		public void set(Type value)
		{
			this.value = value;
		}

		@Override
		public String toString()
		{
			return this.value.toString();
		}
	}

	public static class Tuple3<Type0, Type1, Type2>
	{
		public final Type0 v0;
		public final Type1 v1;
		public final Type2 v2;

		public Tuple3(Type0 v0, Type1 v1, Type2 v2)
		{
			this.v0 = v0;
			this.v1 = v1;
			this.v2 = v2;
		}

		@Override
		public String toString()
		{
			return "(" + this.v0 + ", " + this.v1 + ", " + this.v2 + ")";
		}
	}

	public static class Tuple2Comparable<Type0 extends Comparable<? super Type0>, Type1 extends Comparable<? super Type1>> extends Tuple2<Type0, Type1> implements Comparable<Tuple2Comparable<Type0, Type1>>
	{
		public Tuple2Comparable(Type0 v0, Type1 v1)
		{
			super(v0, v1);
		}

		@Override
		public int compareTo(Tuple2Comparable<Type0, Type1> that)
		{
			int result = this.v0.compareTo(that.v0);
			if (result == 0)
			{
				result = this.v1.compareTo(that.v1);
			}
			return result;
		}
	}

	public static class SingleLinkedList<Type>
	{
		public final Type element;
		public SingleLinkedList<Type> next;

		public SingleLinkedList(Type element, SingleLinkedList<Type> next)
		{
			this.element = element;
			this.next = next;
		}

		public void toCollection(Collection<Type> collection)
		{
			if (this.next != null)
			{
				this.next.toCollection(collection);
			}
			collection.add(this.element);
		}
	}

	public static class Node<Type>
	{
		public static <Type> Node<Type> balance(Node<Type> result)
		{
			while (result != null && 1 < Math.abs(height(result.left) - height(result.right)))
			{
				if (height(result.left) < height(result.right))
				{
					Node<Type> right = result.right;
					if (height(right.right) < height(right.left))
					{
						result = new Node<>(result.value, result.left, right.rotateRight());
					}
					result = result.rotateLeft();
				}
				else
				{
					Node<Type> left = result.left;
					if (height(left.left) < height(left.right))
					{
						result = new Node<>(result.value, left.rotateLeft(), result.right);
					}
					result = result.rotateRight();
				}
			}
			return result;
		}

		public static <Type> Node<Type> clone(Node<Type> result)
		{
			if (result != null)
			{
				result = new Node<>(result.value, clone(result.left), clone(result.right));
			}
			return result;
		}

		public static <Type> Node<Type> delete(Node<Type> node, Type value, Comparator<? super Type> comparator)
		{
			Node<Type> result;
			if (node == null)
			{
				result = null;
			}
			else
			{
				int compare = comparator.compare(value, node.value);
				if (compare == 0)
				{
					if (node.left == null)
					{
						result = node.right;
					}
					else
					{
						if (node.right == null)
						{
							result = node.left;
						}
						else
						{
							Node<Type> first = first(node.right);
							result = new Node<>(first.value, node.left, delete(node.right, first.value, comparator));
						}
					}
				}
				else
				{
					if (compare < 0)
					{
						result = new Node<>(node.value, delete(node.left, value, comparator), node.right);
					}
					else
					{
						result = new Node<>(node.value, node.left, delete(node.right, value, comparator));
					}
				}
				result = balance(result);
			}
			return result;
		}

		public static <Type> Node<Type> first(Node<Type> result)
		{
			while (result.left != null)
			{
				result = result.left;
			}
			return result;
		}

		public static <Type> Node<Type> get(Node<Type> node, Type value, Comparator<? super Type> comparator)
		{
			Node<Type> result;
			if (node == null)
			{
				result = null;
			}
			else
			{
				int compare = comparator.compare(value, node.value);
				if (compare == 0)
				{
					result = node;
				}
				else
				{
					if (compare < 0)
					{
						result = get(node.left, value, comparator);
					}
					else
					{
						result = get(node.right, value, comparator);
					}
				}
			}
			return result;
		}

		public static <Type> Node<Type> head(Node<Type> node, Type value, Comparator<? super Type> comparator)
		{
			Node<Type> result;
			if (node == null)
			{
				result = null;
			}
			else
			{
				int compare = comparator.compare(value, node.value);
				if (compare == 0)
				{
					result = node.left;
				}
				else
				{
					if (compare < 0)
					{
						result = head(node.left, value, comparator);
					}
					else
					{
						result = new Node<>(node.value, node.left, head(node.right, value, comparator));
					}
				}
				result = balance(result);
			}
			return result;
		}

		public static int height(Node node)
		{
			return node == null ? 0 : node.height;
		}

		public static <Type> Node<Type> insert(Node<Type> node, Type value, Comparator<? super Type> comparator)
		{
			Node<Type> result;
			if (node == null)
			{
				result = new Node<>(value, null, null);
			}
			else
			{
				int compare = comparator.compare(value, node.value);
				if (compare == 0)
				{
					result = new Node<>(value, node.left, node.right);
					;
				}
				else
				{
					if (compare < 0)
					{
						result = new Node<>(node.value, insert(node.left, value, comparator), node.right);
					}
					else
					{
						result = new Node<>(node.value, node.left, insert(node.right, value, comparator));
					}
				}
				result = balance(result);
			}
			return result;
		}

		public static <Type> Node<Type> last(Node<Type> result)
		{
			while (result.right != null)
			{
				result = result.right;
			}
			return result;
		}

		public static int size(Node node)
		{
			return node == null ? 0 : node.size;
		}

		public static <Type> Node<Type> tail(Node<Type> node, Type value, Comparator<? super Type> comparator)
		{
			Node<Type> result;
			if (node == null)
			{
				result = null;
			}
			else
			{
				int compare = comparator.compare(value, node.value);
				if (compare == 0)
				{
					result = new Node<>(node.value, null, node.right);
				}
				else
				{
					if (compare < 0)
					{
						result = new Node<>(node.value, tail(node.left, value, comparator), node.right);
					}
					else
					{
						result = tail(node.right, value, comparator);
					}
				}
				result = balance(result);
			}
			return result;
		}

		public static <Type> void traverseOrderIn(Node<Type> node, Consumer<Type> consumer)
		{
			if (node != null)
			{
				traverseOrderIn(node.left, consumer);
				consumer.accept(node.value);
				traverseOrderIn(node.right, consumer);
			}
		}

		public final Type value;
		public final Node<Type> left;
		public final Node<Type> right;
		public final int size;
		private final int height;

		public Node(Type value, Node<Type> left, Node<Type> right)
		{
			this.value = value;
			this.left = left;
			this.right = right;
			this.size = 1 + size(left) + size(right);
			this.height = 1 + Math.max(height(left), height(right));
		}

		public Node<Type> rotateLeft()
		{
			Node<Type> left = new Node<>(this.value, this.left, this.right.left);
			return new Node<>(this.right.value, left, this.right.right);
		}

		public Node<Type> rotateRight()
		{
			Node<Type> right = new Node<>(this.value, this.left.right, this.right);
			return new Node<>(this.left.value, this.left.left, right);
		}
	}

	public static class SortedSetAVL<Type> implements SortedSet<Type>
	{
		public Comparator<? super Type> comparator;
		public Node<Type> root;

		private SortedSetAVL(Comparator<? super Type> comparator, Node<Type> root)
		{
			this.comparator = comparator;
			this.root = root;
		}

		public SortedSetAVL(Comparator<? super Type> comparator)
		{
			this(comparator, null);
		}

		public SortedSetAVL(Collection<? extends Type> collection, Comparator<? super Type> comparator)
		{
			this(comparator, null);
			this.addAll(collection);
		}

		public SortedSetAVL(SortedSetAVL<Type> sortedSetAVL)
		{
			this(sortedSetAVL.comparator, Node.clone(sortedSetAVL.root));
		}

		@Override
		public void clear()
		{
			this.root = null;
		}

		@Override
		public Comparator<? super Type> comparator()
		{
			return this.comparator;
		}

		public Type get(Type value)
		{
			Node<Type> node = Node.get(this.root, value, this.comparator);
			return node == null ? null : node.value;
		}

		@Override
		public SortedSetAVL<Type> subSet(Type valueStart, Type valueEnd)
		{
			return tailSet(valueStart).headSet(valueEnd);
		}

		@Override
		public SortedSetAVL<Type> headSet(Type valueEnd)
		{
			return new SortedSetAVL<>(this.comparator, Node.head(this.root, valueEnd, this.comparator));
		}

		@Override
		public SortedSetAVL<Type> tailSet(Type valueStart)
		{
			return new SortedSetAVL<>(this.comparator, Node.tail(this.root, valueStart, this.comparator));
		}

		@Override
		public Type first()
		{
			return Node.first(this.root).value;
		}

		@Override
		public Type last()
		{
			return Node.last(this.root).value;
		}

		@Override
		public int size()
		{
			return this.root == null ? 0 : this.root.size;
		}

		@Override
		public boolean isEmpty()
		{
			return this.root == null;
		}

		@Override
		public boolean contains(Object value)
		{
			return Node.get(this.root, (Type) value, this.comparator) != null;
		}

		@Override
		public Iterator<Type> iterator()
		{
			Stack<Node<Type>> path = new Stack<>();

			return new Iterator<Type>()
			{
				{
					push(SortedSetAVL.this.root);
				}

				public void push(Node<Type> node)
				{
					while (node != null)
					{
						path.push(node);
						node = node.left;
					}
				}

				@Override
				public boolean hasNext()
				{
					return !path.isEmpty();
				}

				@Override
				public Type next()
				{
					if (path.isEmpty())
					{
						throw new NoSuchElementException();
					}
					else
					{
						Node<Type> node = path.peek();
						Type result = node.value;
						if (node.right != null)
						{
							push(node.right);
						}
						else
						{
							do
							{
								node = path.pop();
							}
							while (!path.isEmpty() && path.peek().right == node);
						}
						return result;
					}
				}
			};
		}

		@Override
		public Object[] toArray()
		{
			List<Object> list = new ArrayList<>();
			Node.traverseOrderIn(this.root, list::add);
			return list.toArray();
		}

		@Override
		public <T> T[] toArray(T[] ts)
		{
			throw new UnsupportedOperationException();
		}

		@Override
		public boolean add(Type value)
		{
			int sizeBefore = size();
			this.root = Node.insert(this.root, value, this.comparator);
			return sizeBefore != size();
		}

		@Override
		public boolean remove(Object value)
		{
			int sizeBefore = size();
			this.root = Node.delete(this.root, (Type) value, this.comparator);
			return sizeBefore != size();
		}

		@Override
		public boolean containsAll(Collection<?> collection)
		{
			return collection.stream()
					.allMatch(this::contains);
		}

		@Override
		public boolean addAll(Collection<? extends Type> collection)
		{
			return collection.stream()
					.map(this::add)
					.reduce(true, (x, y) -> x | y);
		}

		@Override
		public boolean retainAll(Collection<?> collection)
		{
			SortedSetAVL<Type> set = new SortedSetAVL<>(this.comparator);
			collection.stream()
					.map(element -> (Type) element)
					.filter(this::contains)
					.forEach(set::add);
			boolean result = size() != set.size();
			this.root = set.root;
			return result;
		}

		@Override
		public boolean removeAll(Collection<?> collection)
		{
			return collection.stream()
					.map(this::remove)
					.reduce(true, (x, y) -> x | y);
		}

		@Override
		public String toString()
		{
			return "{" + E_418.toString(this, ", ") + "}";
		}
	}

	public static class SortedMapAVL<TypeKey, TypeValue> implements SortedMap<TypeKey, TypeValue>
	{
		public final Comparator<? super TypeKey> comparator;
		public final SortedSetAVL<Entry<TypeKey, TypeValue>> entrySet;

		public SortedMapAVL(Comparator<? super TypeKey> comparator)
		{
			this(comparator, new SortedSetAVL<>((entry0, entry1) -> comparator.compare(entry0.getKey(), entry1.getKey())));
		}

		private SortedMapAVL(Comparator<? super TypeKey> comparator, SortedSetAVL<Entry<TypeKey, TypeValue>> entrySet)
		{
			this.comparator = comparator;
			this.entrySet = entrySet;
		}

		@Override
		public Comparator<? super TypeKey> comparator()
		{
			return this.comparator;
		}

		@Override
		public SortedMapAVL<TypeKey, TypeValue> subMap(TypeKey keyStart, TypeKey keyEnd)
		{
			return new SortedMapAVL<>(this.comparator, this.entrySet.subSet(new AbstractMap.SimpleEntry<>(keyStart, null), new AbstractMap.SimpleEntry<>(keyEnd, null)));
		}

		@Override
		public SortedMapAVL<TypeKey, TypeValue> headMap(TypeKey keyEnd)
		{
			return new SortedMapAVL<>(this.comparator, this.entrySet.headSet(new AbstractMap.SimpleEntry<>(keyEnd, null)));
		}

		@Override
		public SortedMapAVL<TypeKey, TypeValue> tailMap(TypeKey keyStart)
		{
			return new SortedMapAVL<>(this.comparator, this.entrySet.tailSet(new AbstractMap.SimpleEntry<>(keyStart, null)));
		}

		public Entry<TypeKey, TypeValue> firstEntry()
		{
			return this.entrySet.first();
		}

		@Override
		public TypeKey firstKey()
		{
			return firstEntry().getKey();
		}

		public Entry<TypeKey, TypeValue> lastEntry()
		{
			return this.entrySet.last();
		}

		@Override
		public TypeKey lastKey()
		{
			return lastEntry().getKey();
		}

		@Override
		public int size()
		{
			return this.entrySet().size();
		}

		@Override
		public boolean isEmpty()
		{
			return this.entrySet.isEmpty();
		}

		@Override
		public boolean containsKey(Object key)
		{
			return this.entrySet().contains(new AbstractMap.SimpleEntry<>((TypeKey) key, null));
		}

		@Override
		public boolean containsValue(Object value)
		{
			throw new UnsupportedOperationException();
		}

		@Override
		public TypeValue get(Object key)
		{
			Entry<TypeKey, TypeValue> entry = new AbstractMap.SimpleEntry<>((TypeKey) key, null);
			entry = this.entrySet.get(entry);
			return entry == null ? null : entry.getValue();
		}

		@Override
		public TypeValue put(TypeKey key, TypeValue value)
		{
			TypeValue result = get(key);
			Entry<TypeKey, TypeValue> entry = new AbstractMap.SimpleEntry<>(key, value);
			this.entrySet().add(entry);
			return result;
		}

		@Override
		public TypeValue remove(Object key)
		{
			TypeValue result = get(key);
			Entry<TypeKey, TypeValue> entry = new AbstractMap.SimpleEntry<>((TypeKey) key, null);
			this.entrySet.remove(entry);
			return result;
		}

		@Override
		public void putAll(Map<? extends TypeKey, ? extends TypeValue> map)
		{
			map.entrySet()
					.forEach(entry -> put(entry.getKey(), entry.getValue()));
		}

		@Override
		public void clear()
		{
			this.entrySet.clear();
		}

		@Override
		public Set<TypeKey> keySet()
		{
			throw new UnsupportedOperationException();
		}

		@Override
		public Collection<TypeValue> values()
		{
			return new Collection<TypeValue>()
			{
				@Override
				public int size()
				{
					return SortedMapAVL.this.entrySet.size();
				}

				@Override
				public boolean isEmpty()
				{
					return SortedMapAVL.this.entrySet.isEmpty();
				}

				@Override
				public boolean contains(Object value)
				{
					throw new UnsupportedOperationException();
				}

				@Override
				public Iterator<TypeValue> iterator()
				{
					return new Iterator<TypeValue>()
					{
						Iterator<Entry<TypeKey, TypeValue>> iterator = SortedMapAVL.this.entrySet.iterator();

						@Override
						public boolean hasNext()
						{
							return this.iterator.hasNext();
						}

						@Override
						public TypeValue next()
						{
							return this.iterator.next().getValue();
						}
					};
				}

				@Override
				public Object[] toArray()
				{
					throw new UnsupportedOperationException();
				}

				@Override
				public <T> T[] toArray(T[] ts)
				{
					throw new UnsupportedOperationException();
				}

				@Override
				public boolean add(TypeValue typeValue)
				{
					throw new UnsupportedOperationException();
				}

				@Override
				public boolean remove(Object o)
				{
					throw new UnsupportedOperationException();
				}

				@Override
				public boolean containsAll(Collection<?> collection)
				{
					throw new UnsupportedOperationException();
				}

				@Override
				public boolean addAll(Collection<? extends TypeValue> collection)
				{
					throw new UnsupportedOperationException();
				}

				@Override
				public boolean removeAll(Collection<?> collection)
				{
					throw new UnsupportedOperationException();
				}

				@Override
				public boolean retainAll(Collection<?> collection)
				{
					throw new UnsupportedOperationException();
				}

				@Override
				public void clear()
				{
					throw new UnsupportedOperationException();
				}
			};
		}

		@Override
		public SortedSetAVL<Entry<TypeKey, TypeValue>> entrySet()
		{
			return this.entrySet;
		}

		@Override
		public String toString()
		{
			return this.entrySet().toString();
		}
	}

	public static class FIFO<Type>
	{
		public SingleLinkedList<Type> start;
		public SingleLinkedList<Type> end;

		public FIFO()
		{
			this.start = null;
			this.end = null;
		}

		public boolean isEmpty()
		{
			return this.start == null;
		}

		public Type peek()
		{
			return this.start.element;
		}

		public Type pop()
		{
			Type result = this.start.element;
			this.start = this.start.next;
			return result;
		}

		public void push(Type element)
		{
			SingleLinkedList<Type> list = new SingleLinkedList<>(element, null);
			if (this.start == null)
			{
				this.start = list;
				this.end = list;
			}
			else
			{
				this.end.next = list;
				this.end = list;
			}
		}
	}

	public static class MapCount<Type> extends SortedMapAVL<Type, Long>
	{
		private int count;

		public MapCount(Comparator<? super Type> comparator)
		{
			super(comparator);
			this.count = 0;
		}

		public long add(Type key, Long delta)
		{
			long result;
			if (delta > 0)
			{
				Long value = get(key);
				if (value == null)
				{
					value = delta;
				}
				else
				{
					value += delta;
				}
				put(key, value);
				result = delta;
			}
			else
			{
				result = 0;
			}
			this.count += result;
			return result;
		}

		public int count()
		{
			return this.count;
		}

		public List<Type> flatten()
		{
			List<Type> result = new ArrayList<>();
			for (Entry<Type, Long> entry : entrySet())
			{
				for (long index = 0; index < entry.getValue(); index++)
				{
					result.add(entry.getKey());
				}
			}
			return result;
		}

		@Override
		public void putAll(Map<? extends Type, ? extends Long> map)
		{
			throw new UnsupportedOperationException();
		}

		@Override
		public Long remove(Object key)
		{
			Long result = super.remove(key);
			this.count -= result;
			return result;
		}

		public long remove(Type key, Long delta)
		{
			long result;
			if (delta > 0)
			{
				Long value = get(key) - delta;
				if (value <= 0)
				{
					result = delta + value;
					remove(key);
				}
				else
				{
					result = delta;
					put(key, value);
				}
			}
			else
			{
				result = 0;
			}
			this.count -= result;
			return result;
		}

		@Override
		public SortedMapAVL<Type, Long> subMap(Type keyStart, Type keyEnd)
		{
			throw new UnsupportedOperationException();
		}

		@Override
		public SortedMapAVL<Type, Long> headMap(Type keyEnd)
		{
			throw new UnsupportedOperationException();
		}

		@Override
		public SortedMapAVL<Type, Long> tailMap(Type keyStart)
		{
			throw new UnsupportedOperationException();
		}
	}

	public static class MapSet<TypeKey, TypeValue> extends SortedMapAVL<TypeKey, SortedSetAVL<TypeValue>> implements Iterable<TypeValue>
	{
		private Comparator<? super TypeValue> comparatorValue;

		public MapSet(Comparator<? super TypeKey> comparatorKey, Comparator<? super TypeValue> comparatorValue)
		{
			super(comparatorKey);
			this.comparatorValue = comparatorValue;
		}

		public MapSet(Comparator<? super TypeKey> comparatorKey, SortedSetAVL<Entry<TypeKey, SortedSetAVL<TypeValue>>> entrySet, Comparator<? super TypeValue> comparatorValue)
		{
			super(comparatorKey, entrySet);
			this.comparatorValue = comparatorValue;
		}

		public TypeValue firstValue()
		{
			TypeValue result;
			Entry<TypeKey, SortedSetAVL<TypeValue>> firstEntry = firstEntry();
			if (firstEntry == null)
			{
				result = null;
			}
			else
			{
				result = firstEntry.getValue().first();
			}
			return result;
		}

		public Iterator<TypeValue> iterator()
		{
			return new Iterator<TypeValue>()
			{
				Iterator<SortedSetAVL<TypeValue>> iteratorValues = values().iterator();
				Iterator<TypeValue> iteratorValue = null;

				@Override
				public boolean hasNext()
				{
					return iteratorValues.hasNext() || (iteratorValue != null && iteratorValue.hasNext());
				}

				@Override
				public TypeValue next()
				{
					if (iteratorValue == null || !iteratorValue.hasNext())
					{
						iteratorValue = iteratorValues.next().iterator();
					}
					return iteratorValue.next();
				}
			};
		}

		public TypeValue lastValue()
		{
			TypeValue result;
			Entry<TypeKey, SortedSetAVL<TypeValue>> lastEntry = lastEntry();
			if (lastEntry == null)
			{
				result = null;
			}
			else
			{
				result = lastEntry.getValue().last();
			}
			return result;
		}

		public boolean add(TypeKey key, TypeValue value)
		{
			SortedSetAVL<TypeValue> set = computeIfAbsent(key, k -> new SortedSetAVL<>(comparatorValue));
			return set.add(value);
		}

		public boolean removeSet(TypeKey key, TypeValue value)
		{
			boolean result;
			SortedSetAVL<TypeValue> set = get(key);
			if (set == null)
			{
				result = false;
			}
			else
			{
				result = set.remove(value);
				if (set.size() == 0)
				{
					remove(key);
				}
			}
			return result;
		}

		@Override
		public MapSet<TypeKey, TypeValue> headMap(TypeKey keyEnd)
		{
			return new MapSet<>(this.comparator, this.entrySet.headSet(new AbstractMap.SimpleEntry<>(keyEnd, null)), this.comparatorValue);
		}

		@Override
		public MapSet<TypeKey, TypeValue> tailMap(TypeKey keyStart)
		{
			return new MapSet<>(this.comparator, this.entrySet.tailSet(new AbstractMap.SimpleEntry<>(keyStart, null)), this.comparatorValue);
		}
	}

	static class IteratorBuffer<Type>
	{
		private Iterator<Type> iterator;
		private List<Type> list;

		public IteratorBuffer(Iterator<Type> iterator)
		{
			this.iterator = iterator;
			this.list = new ArrayList<Type>();
		}

		public Iterator<Type> iterator()
		{
			return new Iterator<Type>()
			{
				int index = 0;

				@Override
				public boolean hasNext()
				{
					return this.index < list.size() || iterator().hasNext();
				}

				@Override
				public Type next()
				{
					if (list.size() <= this.index)
					{
						list.add(iterator.next());
					}
					Type result = list.get(index);
					index += 1;
					return result;
				}
			};
		}
	}

	public static <Type> List<List<Type>> permutations(List<Type> list)
	{
		List<List<Type>> result = new ArrayList<>();
		result.add(new ArrayList<>());
		for (Type element : list)
		{
			List<List<Type>> permutations = result;
			result = new ArrayList<>();
			for (List<Type> permutation : permutations)
			{
				for (int index = 0; index <= permutation.size(); index++)
				{
					List<Type> permutationNew = new ArrayList<>(permutation);
					permutationNew.add(index, element);
					result.add(permutationNew);
				}
			}
		}
		return result;
	}

	public static List<List<Integer>> combinations(int n, int k)
	{
		List<List<Integer>> result = new ArrayList<>();
		if (k == 0)
		{
		}
		else
		{
			if (k == 1)
			{
				List<Integer> combination = new ArrayList<>();
				combination.add(n);
				result.add(combination);
			}
			else
			{
				for (int index = 0; index <= n; index++)
				{
					for (List<Integer> combination : combinations(n - index, k - 1))
					{
						combination.add(index);
						result.add(combination);
					}
				}
			}
		}
		return result;
	}

	public static <Type> int compare(Iterator<Type> iterator0, Iterator<Type> iterator1, Comparator<Type> comparator)
	{
		int result = 0;
		while (result == 0 && iterator0.hasNext() && iterator1.hasNext())
		{
			result = comparator.compare(iterator0.next(), iterator1.next());
		}
		if (result == 0)
		{
			if (iterator1.hasNext())
			{
				result = -1;
			}
			else
			{
				if (iterator0.hasNext())
				{
					result = 1;
				}
			}
		}
		return result;
	}

	public static <Type> int compare(Iterable<Type> iterable0, Iterable<Type> iterable1, Comparator<Type> comparator)
	{
		return compare(iterable0.iterator(), iterable1.iterator(), comparator);
	}

	private static String nextString() throws IOException
	{
		while ((stringTokenizer == null) || (!stringTokenizer.hasMoreTokens()))
		{
			stringTokenizer = new StringTokenizer(bufferedReader.readLine());
		}
		return stringTokenizer.nextToken();
	}

	private static String[] nextStrings(int n) throws IOException
	{
		String[] result = new String[n];
		{
			for (int index = 0; index < n; index++)
			{
				result[index] = nextString();
			}
		}
		return result;
	}

	public static int nextInt() throws IOException
	{
		return Integer.parseInt(nextString());
	}

	public static int[] nextInts(int n) throws IOException
	{
		int[] result = new int[n];
		{
			for (int index = 0; index < n; index++)
			{
				result[index] = nextInt();
			}
		}
		return result;
	}

	public static double nextDouble() throws IOException
	{
		return Double.parseDouble(nextString());
	}

	public static long nextLong() throws IOException
	{
		return Long.parseLong(nextString());
	}

	public static long[] nextLongs(int n) throws IOException
	{
		long[] result = new long[n];
		{
			for (int index = 0; index < n; index++)
			{
				result[index] = nextLong();
			}
		}
		return result;
	}

	public static String nextLine() throws IOException
	{
		return bufferedReader.readLine();
	}

	public static void close()
	{
		out.close();
	}

	public static int binarySearchMinimum(Function<Integer, Boolean> filter, int start, int end)
	{
		int result;
		if (start == end)
		{
			result = end;
		}
		else
		{
			int middle = start + (end - start) / 2;
			if (filter.apply(middle))
			{
				result = binarySearchMinimum(filter, start, middle);
			}
			else
			{
				result = binarySearchMinimum(filter, middle + 1, end);
			}
		}
		return result;
	}

	public static int binarySearchMaximum(Function<Integer, Boolean> filter, int start, int end)
	{
		return -binarySearchMinimum(x -> filter.apply(-x), -end, -start);
	}

	public static long divideCeil(long x, long y)
	{
		return (x + y - 1) / y;
	}

	public static Set<Long> divisors(long n)
	{
		SortedSetAVL<Long> result = new SortedSetAVL<>(Comparator.naturalOrder());
		result.add(1L);
		for (Long factor : factors(n))
		{
			SortedSetAVL<Long> divisors = new SortedSetAVL<>(result);
			for (Long divisor : result)
			{
				divisors.add(divisor * factor);
			}
			result = divisors;
		}
		return result;
	}

	public static BigInteger facultyBig(int n)
	{
		BigInteger result = BigInteger.ONE;
		for (int index = 2; index <= n; index++)
		{
			result = result.multiply(BigInteger.valueOf(index));
		}
		return result;
	}

	public static long faculty(int n)
	{
		long result = 1;
		for (int index = 2; index <= n; index++)
		{
			result *= index;
		}
		return result;
	}


	public static LinkedList<Long> factors(long n)
	{
		LinkedList<Long> result = new LinkedList<>();
		Iterator<Long> primes = ITERATOR_BUFFER_PRIME.iterator();
		Long prime;
		while (n > 1 && (prime = primes.next()) * prime <= n)
		{
			while (n % prime == 0)
			{
				result.add(prime);
				n /= prime;
			}
		}
		if (n > 1)
		{
			result.add(n);
		}
		return result;
	}

	public static long gcd(long a, long b)
	{
		while (a != 0 && b != 0)
		{
			if (a > b)
			{
				a %= b;
			}
			else
			{
				b %= a;
			}
		}
		return a + b;
	}

	public static long[] generatePOWER2()
	{
		long[] result = new long[63];
		for (int x = 0; x < result.length; x++)
		{
			result[x] = 1L << x;
		}
		return result;
	}

	public static BigInteger[] generateFacultyBig()
	{
		BigInteger[] result = new BigInteger[50];
		for (int x = 0; x < result.length; x++)
		{
			result[x] = facultyBig(x);
		}
		return result;
	}

	public static boolean isPrime(long x)
	{
		boolean result = x > 1;
		Iterator<Long> iterator = ITERATOR_BUFFER_PRIME.iterator();
		Long prime;
		while ((prime = iterator.next()) * prime <= x)
		{
			result &= x % prime > 0;
		}
		return result;
	}

	public static long knapsack(List<Tuple3<Long, Integer, Integer>> itemsValueWeightCount, int weightMaximum)
	{
		long[] valuesMaximum = new long[weightMaximum + 1];
		for (Tuple3<Long, Integer, Integer> itemValueWeightCount : itemsValueWeightCount)
		{
			long itemValue = itemValueWeightCount.v0;
			int itemWeight = itemValueWeightCount.v1;
			int itemCount = itemValueWeightCount.v2;
			for (int weight = weightMaximum; 0 <= weight; weight--)
			{
				for (int index = 1; index <= itemCount && 0 <= weight - index * itemWeight; index++)
				{
					valuesMaximum[weight] = Math.max(valuesMaximum[weight], valuesMaximum[weight - index * itemWeight] + index * itemValue);
				}
			}
		}
		long result = 0;
		for (long valueMaximum : valuesMaximum)
		{
			result = Math.max(result, valueMaximum);
		}
		return result;
	}

	public static boolean knapsackPossible(List<Tuple2<Integer, Integer>> itemsWeightCount, int weightMaximum)
	{
		boolean[] weightPossible = new boolean[weightMaximum + 1];
		weightPossible[0] = true;
		int weightLargest = 0;
		for (Tuple2<Integer, Integer> itemWeightCount : itemsWeightCount)
		{
			int itemWeight = itemWeightCount.v0;
			int itemCount = itemWeightCount.v1;
			for (int weightStart = 0; weightStart < itemWeight; weightStart++)
			{
				int count = 0;
				for (int weight = weightStart; weight <= weightMaximum && (0 < count || weight <= weightLargest); weight += itemWeight)
				{
					if (weightPossible[weight])
					{
						count = itemCount;
					}
					else
					{
						if (0 < count)
						{
							weightPossible[weight] = true;
							weightLargest = weight;
							count -= 1;
						}
					}
				}
			}
		}
		return weightPossible[weightMaximum];
	}

	public static long lcm(int a, int b)
	{
		return a * b / gcd(a, b);
	}

	public static <T> List<T> permutation(long p, List<T> x)
	{
		List<T> copy = new ArrayList<>();
		for (int index = 0; index < x.size(); index++)
		{
			copy.add(x.get(index));
		}
		List<T> result = new ArrayList<>();
		for (int indexTo = 0; indexTo < x.size(); indexTo++)
		{
			int indexFrom = (int) p % copy.size();
			p = p / copy.size();
			result.add(copy.remove(indexFrom));
		}
		return result;
	}

	public static <Type> String toString(Iterator<Type> iterator, String separator)
	{
		StringBuilder stringBuilder = new StringBuilder();
		if (iterator.hasNext())
		{
			stringBuilder.append(iterator.next());
		}
		while (iterator.hasNext())
		{
			stringBuilder.append(separator);
			stringBuilder.append(iterator.next());
		}
		return stringBuilder.toString();
	}

	public static <Type> String toString(Iterator<Type> iterator)
	{
		return toString(iterator, " ");
	}

	public static <Type> String toString(Iterable<Type> iterable, String separator)
	{
		return toString(iterable.iterator(), separator);
	}

	public static <Type> String toString(Iterable<Type> iterable)
	{
		return toString(iterable, " ");
	}

	public static Stream<BigInteger> streamFibonacci()
	{
		return Stream.generate(new Supplier<BigInteger>()
		{
			private BigInteger n0 = BigInteger.ZERO;
			private BigInteger n1 = BigInteger.ONE;

			@Override
			public BigInteger get()
			{
				BigInteger result = n0;
				n0 = n1;
				n1 = result.add(n0);
				return result;
			}
		});
	}

	public static Stream<Long> streamPrime(int sieveSize)
	{
		return Stream.generate(new Supplier<Long>()
		{
			private boolean[] isPrime = new boolean[sieveSize];
			private long sieveOffset = 2;
			private List<Long> primes = new ArrayList<>();
			private int index = 0;

			public void filter(long prime, boolean[] result)
			{
				if (prime * prime < this.sieveOffset + sieveSize)
				{
					long remainingStart = this.sieveOffset % prime;
					long start = remainingStart == 0 ? 0 : prime - remainingStart;
					for (long index = start; index < sieveSize; index += prime)
					{
						result[(int) index] = false;
					}
				}
			}

			public void generatePrimes()
			{
				Arrays.fill(this.isPrime, true);
				this.primes.forEach(prime -> filter(prime, isPrime));
				for (int index = 0; index < sieveSize; index++)
				{
					if (isPrime[index])
					{
						this.primes.add(this.sieveOffset + index);
						filter(this.sieveOffset + index, isPrime);
					}
				}
				this.sieveOffset += sieveSize;
			}

			@Override
			public Long get()
			{
				while (this.primes.size() <= this.index)
				{
					generatePrimes();
				}
				Long result = this.primes.get(this.index);
				this.index += 1;
				return result;
			}
		});
	}

	public static long totient(long n)
	{
		Set<Long> factors = new SortedSetAVL<>(factors(n), Comparator.naturalOrder());
		long result = n;
		for (long p : factors)
		{
			result -= result / p;
		}
		return result;
	}

	public static void main(String[] args)
	{
		try
		{
			solve();
		} catch (IOException exception)
		{
			exception.printStackTrace();
		}
		close();
	}

	public static void add(int p1, int p2, int c1, int c2, long count, long[][][][] result)
	{
		if (p1 >= 0 && p2 >= 0 && c1 >= 0 && c2 >= 0 && count > 0)
		{
			if (p1 < result.length && p2 < result[p1].length && c1 < result[p1][p2].length && c2 < result[p1][p2][c1].length)
			{
				result[p1][p2][c1][c2] += count;
			}
		}
	}

	public static void addPrevious(int p1, int p2, int c1, int c2, long count, long[][][][] result)
	{
		add(p1 - 1, p2, c1, c2, p1 * count, result);
		add(p1 + 1, p2 - 1, c1, c2, p2 * count, result);
	}

	public static void next(int d, long count, int p1, int p2, int c1, int c2, long[][][][] result)
	{
		if (p1 == 0 && p2 == 0)
		{
			if (d == 2)
			{
				addPrevious(c1, c2, 1, 0, count, result);
			}
			else
			{
				addPrevious(c1, c2, 0, 1, count, result);
			}
		}

		if (d == 2)
		{
			addPrevious(p1, p2, c1 + 1, c2, count, result);

			addPrevious(p1, p2, c1 - 1, c2, c1 * count, result);
			addPrevious(p1, p2, c1 + 1, c2 - 1, c2 * count, result);
		}
		else
		{
			addPrevious(p1, p2, c1, c2 + 1, count, result);

			addPrevious(p1, p2, c1, c2, c1 * count, result);
			addPrevious(p1, p2, c1 + 2, c2 - 1, c2 * count, result);

			addPrevious(p1, p2, c1 - 2, c2, c1 * (c1 - 1) / 2 * count, result);
			addPrevious(p1, p2, c1, c2 - 1, c1 * c2 * count, result);
			addPrevious(p1, p2, c1 + 2, c2 - 2, c2 * (c2 - 1) / 2 * count, result);
		}
	}

	public static long solve(int[] d)
	{
		long[][][][] count = new long[d.length / 2 + 1][d.length / 2 + 1][d.length / 2 + 1][d.length / 2 + 1];
		if (d[0] == 2)
		{
			if (d[1] == 2)
			{
				count[1][0][1][0] = 1;
			}
			else
			{
				count[1][0][0][1] = 1;
			}
		}
		else
		{
			if (d[1] == 2)
			{
				count[0][1][1][0] = 1;
			}
			else
			{
				count[0][1][0][1] = 1;
			}
		}
		for (int u = 2; u < d.length; u++)
		{
			long[][][][] countNext = new long[d.length / 2 + 1][d.length / 2 + 1][d.length / 2 + 1][d.length / 2 + 1];
			for (int p1 = 0; p1 <= d.length / 2; p1++)
			{
				for (int p2 = 0; p2 <= d.length / 2 && p1 + p2 < d.length; p2++)
				{
					for (int c1 = 0; c1 <= d.length / 2 && p1 + p2 + c1 < d.length; c1++)
					{
						for (int c2 = 0; c2 <= d.length / 2 && p1 + p2 + c1 + c2 < d.length; c2++)
						{
							next(d[u], count[p1][p2][c1][c2] % BIG, p1, p2, c1, c2, countNext);
						}
					}
				}
			}
			count = countNext;
		}
		return count[0][0][0][0] % BIG;
	}

	public static void solve() throws IOException
	{
		int n = nextInt();
		int[] d = nextInts(n);
		out.println(solve(d));
	}
}