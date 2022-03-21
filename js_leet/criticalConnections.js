// There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections
// forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi.

// Any server can reach other servers directly or indirectly through the network.

// A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

// Return all critical connections in the network in any order.


// 2 <= n <= 105
// n - 1 <= connections.length <= 105
// 0 <= ai, bi <= n - 1
// ai != bi
// There are no repeated connections.


// Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
// Output: [[1,3]]
// Explanation: [[3,1]] is also accepted.

// Input: n = 2, connections = [[0,1]]
// Output: [[0,1]]


/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number[][]}
 */
 var criticalConnections = function(n, connections) {
	 // okay - how does one determine that a connection is critical
	 // a connection is critical if a node has only a single connection
	 // map each node, counting its number of vertices
	 let countMap = new Map();
	 let connectionMap = new Map();

	 connections.forEach((connection) => {
		 connectionMap.set(connection[0], []);
		 connectionMap.set(connection[1], []);
	 });


	 connections.forEach((connection) => {
		 let c1 = connection[0], c2 = connection[1];
		 if (countMap.get(c1)) {
			countMap.set(c1, countMap.get(c1) + 1);
		 } else {
			 countMap.set(c1, 1);
		 }
		 if (countMap.get(c2)) {
			countMap.set(c2, countMap.get(c2) + 1);
		 } else {
			 countMap.set(c2, 1);
		 }
		 let c1Connections = connectionMap.get(c1);
		 let c2Connections = connectionMap.get(c2);
		 c1Connections.push(connection);
		 c2Connections.push(connection);

		//  console.log({c1Connections, c2Connections});
		 connectionMap.set(c1, c1Connections);
		 connectionMap.set(c2, c2Connections);
	 })

	//  nodeMap.forEach((v, k) => console.log({k:k, v:v}));
	// connectionMap.forEach((v,k) => console.log({k:k, v:v}));

	let critical= [];
	countMap.forEach((v,k) => {
		if (v == 1) {
			// this was a critical connection
			let con = connectionMap.get(k)[0];
			if (!critical.includes(con)) {

				critical.push(con);
			}
		}
	});

	return critical;

};

let n = 4, connections = [[0,1],[1,2],[2,0],[1,3]];
n = 2, connections = [[0,1]];

console.log(criticalConnections(n, connections));