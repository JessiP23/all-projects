/*if (
    user.age >= movie.ageLimit &&
    movie.isAvailableInCountry(user.country) &&
    !movie.isRestrictedToPremiumUsers
){}
*/

let isOldEnough = user.age >= movie.ageLimit;
let isInAvailableCountry = movie.isAvailableInCountry(user.country);
let isNotRestrictedMovie = !movie.isRestrictedToPremiumUsers;
let canWatchMovie = isOldEnough && isInAvailableCountry && isNotRestrictedMovie
if(canWatchMovie){

}


/*
let user = null;
if(user && user.isLoggedIn){
}
use = {name:"John Doe"};
let displayName = user.name || "Guest";
*/