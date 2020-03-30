from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required
from eusoffline.election.forms import TestForm
from eusoffline import db
from eusoffline.models import Candidates, Votes

election = Blueprint('election', __name__)


@election.route("/election/rules", methods=['GET'])
def electionrules():
    return render_template('/election/electionrules.html')


@election.route("/election", methods=['GET'])
def electionHome():
    return render_template('/election/electionindex.html')


"""
    1. Vote all or not vote at all
    2. Y/N for all candidates
    3. embed video links
    4. image will be static (for AY2019/20)
"""
@login_required
@election.route("/election/voting/<category>/<id>/<state>",
                methods=['GET', 'POST'])
def electionVoting(category, id, state):

    # if the current user has already voted, kick him the fuck out
    votes = Votes.query.filter_by(voter=current_user.matric).all()
    for vote in votes:
        candidate = Candidates.query.filter_by(id=vote.target_id).first()
        if (candidate.category == category):
            return redirect(url_for('election.electionConfirmVotes',
                                    category=category))

    candidates = Candidates.query.filter_by(
        category=category).all()

    # context setting
    candidate_index = 1
    candidate_dict = {}
    for candidate in candidates:
        candidate_dict[candidate_index] = candidate
        candidate_index += 1

    last_candidate = False
    if (int(id) == candidate_index - 1):
        last_candidate = True

    this_candidate = candidate_dict[int(id)]
    form = TestForm()

    if request.method == 'POST':
        if (int(id) < candidate_index-1):
            if (state == '0'):
                new_state = id + ":" + form.votes.data + "?"
            else:
                new_state = state + id + ":" + form.votes.data

            new_id = int(id) + 1
            if (int(id) == candidate_index-1):
                return redirect(url_for('election.electionVoting',
                                        category=category, id=new_id,
                                        state=new_state))
            else:
                return redirect(url_for('election.electionVoting',
                                        category=category, id=new_id,
                                        state=new_state))
        else:
            # previously registered data
            all_votes = {}
            tokens = state.split('?')
            for token in tokens:
                vote = token.split(':')
                this_candidate = candidate_dict[int(vote[0])]

                if (vote[1] == "yes"):
                    all_votes[this_candidate.id] = "1"
                else:
                    all_votes[this_candidate.id] = "0"

            # last candidate
            this_candidate = candidate_dict[int(id)]
            if (form.votes.data == "yes"):
                all_votes[int(id)] = "1"
            else:
                all_votes[int(id)] = "0"

            # voter, target_id, 1/0 to indicate y/n
            for i in all_votes:
                voter_id = current_user.matric
                new_vote = Votes(
                    voter=voter_id, target_id=i, vote=all_votes[i])
                db.session.add(new_vote)

            db.session.commit()

            return redirect(url_for('election.electionConfirmVotes',
                                    category=category))

    return render_template('/election/votingpage.html', form=form,
                           candidate=this_candidate,
                           last_candidate=last_candidate)


@login_required
@election.route("/election/voting/confirmation/<category>",
                methods=['GET', 'POST'])
def electionConfirmVotes(category):
    votes = Votes.query.filter_by(voter=current_user.matric).all()
    display_vote = {}

    for vote in votes:
        candidate = Candidates.query.filter_by(id=vote.target_id).first()
        if (candidate.category == category):
            if vote.vote == 1:
                display_vote[candidate.name] = {
                    'vote': 'YES', 'id': candidate.id}
            else:
                display_vote[candidate.name] = {'vote': 'NO', 'id': candidate.id}

    return render_template('/election/votingConfirm.html',
                           display_vote=display_vote, category=category)
