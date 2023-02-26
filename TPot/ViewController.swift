//
//  ViewController.swift
//  TPot
//
//  Created by Aditi Bansal on 2/25/23.
//

import UIKit
import FirebaseFirestore

class ViewController: UIViewController {

    @IBOutlet weak var tableView: UITableView!
    let db = Firestore.firestore()
    
    var temps: [Temp] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView.dataSource = self
        loadData()
        // Do any additional setup after loading the view.
    }
    
    func loadData() {
        db.collection("temps")
            .order(by: "time")
            .addSnapshotListener { FIRQuerySnapshot, error in
            
            self.temps = []
            
            if let e = error {
                print("There was an issue retrieving data from Firestore. \(e)")
            } else {
                if let snapshotDocuments = FIRQuerySnapshot?.documents {
                    for doc in snapshotDocuments {
                        let data = doc.data()
                        if let tempTime = data["time"] as? Int, let tempMessage = data["temp"] as? Int {
                            let newTemp = Temp(time: tempTime, temp: tempMessage)
                            self.temps.append(newTemp)
                            
                            DispatchQueue.main.async {
                                self.tableView.reloadData()
                                //let indexPath = IndexPath(row: self.temps.count - 1, section: 0)
                                //self.tableView.scrollToRow(at: indexPath, at: .top, animated: false)
                            }
                        }
                    }
                }
            }
        }
    }
    


}

extension ViewController: UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return temps.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let t = temps[indexPath.row]
        
        let cell = tableView.dequeueReusableCell(withIdentifier: "ReusableCell", for: indexPath)
        cell.textLabel?.text = String(t.temp)
        print(t.temp)
        
        
        return cell
    }
}

