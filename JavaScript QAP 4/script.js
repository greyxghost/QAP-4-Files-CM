// Define the Customer Object 

const custInfo = {
    custFirst: "Count",
    custLast: "Dracula",
    custBirth: "1432-12-01",
    gender: "Male",
    roomPref: ["Single Bed", "Non-Smoking", "No Garlic"],
    payMethod: "Credit Card",

    custAddress: {
        street: "123 Scary Street",
        city: "Spooky City",
        province: "NL",
        postal: "A0A 1L9"
    },

    phoneNum: "709-999-1212",
    
    checkIn: {
        date: "2024-10-23",
        time: "15:00",
    },
    checkOut: {
        date: "2024-10-26",
        time: "15:00",
    },

    // Method to calculate age
    calcAge: function() {
        const today = new Date();
        const birthDate = new Date(this.custBirth);
        let age = today.getFullYear() - birthDate.getFullYear();
        const monthDiff = today.getMonth() - birthDate.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }
        return age;
    },

     // Method to calculate duration of stay
     calcDurOfStay: function() {
        const checkInDate = new Date(this.checkIn.date);
        const checkOutDate = new Date(this.checkOut.date);
        const duration = (checkOutDate - checkInDate) / (1000 * 60 * 60 * 24); // Convert milliseconds to days
        return duration;
    },

     // Method to generate description
     custDescription: function() {
        return `Today we have a special guest joining us. ${this.custFirst} ${this.custLast}, who was born ${this.custBirth}, 
        usually stays with us through out the year, prefers a room with the following: <strong>${this.roomPref.join(', ')} </strong>. <br/>
        He will be paying by <strong>${this.payMethod}</strong> and all other room charges can go to this card. 
        He will be coming on <strong>${this.checkIn.date}</strong> at <strong>${this.checkIn.time}</strong> and leaving at
        <strong>${this.checkOut.date}</strong> at <strong>${this.checkOut.time}</strong>. We ask you to make his stay enjoyable. `;
    },

     // Method to generate HTML Description for the Customer!
     custGenHTML: function() {
        return `
            <div>
                <h2>Customer Information</h2>
                <p><strong>Name:</strong> ${this.custFirst} ${this.custLast}</p>
                <p><strong>Date of Birth:</strong> ${this.custBirth} (${this.calcAge()} years old)</p>
                <p><strong>Gender:</strong> ${this.gender}</p>
                <p><strong>Room Preferences:</strong> ${this.roomPref.join(', ')}</p>
                <p><strong>Payment Methods:</strong> ${this.payMethod}</p>
                <p><strong>Address:</strong> ${this.custAddress.street}, ${this.custAddress.city}, ${this.custAddress.province}, ${this.custAddress.postal}</p>
                <p><strong>Phone Number:</strong> ${this.phoneNum}</p>
                <p><strong>Check-In:</strong> ${this.checkIn.date} at ${this.checkIn.time}</p>
                <p><strong>Check-Out:</strong> ${this.checkOut.date} at ${this.checkOut.time}</p>
                <p><strong>Duration of Stay:</strong> ${this.calcDurOfStay()} days</p>
            </div>
        `;
    }

}

console.log(custInfo);
console.log("Description: ", custInfo.custDescription());
console.log("Age: ", custInfo.calcAge());
console.log("Duration of Stay: ", custInfo.calcDurOfStay(), "days");
console.log("HTML: ", custInfo.custGenHTML());
document.write(custInfo.custDescription())
document.write(custInfo.custGenHTML())

