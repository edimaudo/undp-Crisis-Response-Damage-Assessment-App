def award_points(db, user, points):
    user.points += points
    db.commit()
