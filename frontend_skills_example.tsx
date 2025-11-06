// Example React component for browsing and adding skills
// This shows how the skills API can be used in the frontend

import React, { useState, useEffect } from 'react';

interface Skill {
  id: string;
  name: string;
  category: string;
  proficiency_level?: number;
}

interface SkillCategory {
  [category: string]: Skill[];
}

const SkillsBrowser: React.FC = () => {
  const [categories, setCategories] = useState<SkillCategory>({});
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState<Skill[]>([]);
  const [popularSkills, setPopularSkills] = useState<Skill[]>([]);
  const [userSkills, setUserSkills] = useState<Skill[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<string>('');
  const [loading, setLoading] = useState(false);

  // Fetch popular skills on component mount
  useEffect(() => {
    fetchPopularSkills();
    fetchUserSkills();
  }, []);

  const fetchPopularSkills = async () => {
    try {
      const response = await fetch('/api/skills/popular?limit=20');
      const data = await response.json();
      if (data.success) {
        setPopularSkills(data.skills);
      }
    } catch (error) {
      console.error('Error fetching popular skills:', error);
    }
  };

  const fetchUserSkills = async () => {
    try {
      const userId = getCurrentUserId(); // Implement this function
      const response = await fetch(`/api/users/${userId}/skills`);
      const data = await response.json();
      if (data.success) {
        setUserSkills(data.skills);
      }
    } catch (error) {
      console.error('Error fetching user skills:', error);
    }
  };

  const fetchCategories = async () => {
    try {
      setLoading(true);
      const response = await fetch('/api/skills/categories');
      const data = await response.json();
      if (data.success) {
        setCategories(data.categories);
      }
    } catch (error) {
      console.error('Error fetching categories:', error);
    } finally {
      setLoading(false);
    }
  };

  const searchSkills = async (query: string) => {
    if (query.length < 2) {
      setSearchResults([]);
      return;
    }

    try {
      const response = await fetch(`/api/skills/search?q=${encodeURIComponent(query)}&limit=20`);
      const data = await response.json();
      if (data.success) {
        setSearchResults(data.skills);
      }
    } catch (error) {
      console.error('Error searching skills:', error);
    }
  };

  const addSkillToUser = async (skillId: string, proficiencyLevel: number = 3) => {
    try {
      const userId = getCurrentUserId();
      const response = await fetch(`/api/users/${userId}/skills`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          skill_id: skillId,
          proficiency_level: proficiencyLevel,
        }),
      });

      const data = await response.json();
      if (data.success) {
        fetchUserSkills(); // Refresh user skills
        alert('Skill added successfully!');
      } else {
        alert(data.error || 'Failed to add skill');
      }
    } catch (error) {
      console.error('Error adding skill:', error);
      alert('Failed to add skill');
    }
  };

  const removeSkillFromUser = async (skillId: string) => {
    try {
      const userId = getCurrentUserId();
      const response = await fetch(`/api/users/${userId}/skills/${skillId}`, {
        method: 'DELETE',
      });

      const data = await response.json();
      if (data.success) {
        fetchUserSkills(); // Refresh user skills
        alert('Skill removed successfully!');
      } else {
        alert(data.error || 'Failed to remove skill');
      }
    } catch (error) {
      console.error('Error removing skill:', error);
      alert('Failed to remove skill');
    }
  };

  const handleSearchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const query = e.target.value;
    setSearchQuery(query);
    searchSkills(query);
  };

  const isSkillAdded = (skillId: string) => {
    return userSkills.some(skill => skill.id === skillId);
  };

  const getCurrentUserId = () => {
    // Implement this to get current user ID from your auth system
    return 'current-user-id';
  };

  const SkillCard: React.FC<{ skill: Skill; showCategory?: boolean }> = ({ 
    skill, 
    showCategory = false 
  }) => (
    <div className="skill-card border rounded-lg p-3 m-2 bg-white shadow-sm">
      <div className="flex justify-between items-center">
        <div>
          <h4 className="font-medium text-gray-900">{skill.name}</h4>
          {showCategory && (
            <p className="text-sm text-gray-500">{skill.category}</p>
          )}
          {skill.proficiency_level && (
            <div className="flex items-center mt-1">
              <span className="text-xs text-gray-500 mr-2">Level:</span>
              <div className="flex">
                {[1, 2, 3, 4, 5].map(level => (
                  <div
                    key={level}
                    className={`w-3 h-3 rounded-full mr-1 ${
                      level <= skill.proficiency_level! 
                        ? 'bg-blue-500' 
                        : 'bg-gray-200'
                    }`}
                  />
                ))}
              </div>
            </div>
          )}
        </div>
        <div>
          {isSkillAdded(skill.id) ? (
            <button
              onClick={() => removeSkillFromUser(skill.id)}
              className="px-3 py-1 text-sm bg-red-500 text-white rounded hover:bg-red-600"
            >
              Remove
            </button>
          ) : (
            <button
              onClick={() => addSkillToUser(skill.id)}
              className="px-3 py-1 text-sm bg-blue-500 text-white rounded hover:bg-blue-600"
            >
              Add
            </button>
          )}
        </div>
      </div>
    </div>
  );

  return (
    <div className="skills-browser max-w-6xl mx-auto p-6">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">Browse Skills</h1>

      {/* Search Section */}
      <div className="mb-8">
        <div className="relative">
          <input
            type="text"
            placeholder="Search skills (e.g., React, Python, Design)..."
            value={searchQuery}
            onChange={handleSearchChange}
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
          <div className="absolute inset-y-0 right-0 pr-3 flex items-center">
            <svg className="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
          </div>
        </div>

        {/* Search Results */}
        {searchQuery && searchResults.length > 0 && (
          <div className="mt-4">
            <h3 className="text-lg font-semibold mb-3">Search Results ({searchResults.length})</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2">
              {searchResults.map(skill => (
                <SkillCard key={skill.id} skill={skill} showCategory={true} />
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Your Skills Section */}
      {userSkills.length > 0 && (
        <div className="mb-8">
          <h2 className="text-2xl font-semibold text-gray-900 mb-4">Your Skills ({userSkills.length})</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2">
            {userSkills.map(skill => (
              <SkillCard key={skill.id} skill={skill} showCategory={true} />
            ))}
          </div>
        </div>
      )}

      {/* Popular Skills Section */}
      <div className="mb-8">
        <h2 className="text-2xl font-semibold text-gray-900 mb-4">Popular Skills</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2">
          {popularSkills.map(skill => (
            <SkillCard key={skill.id} skill={skill} showCategory={true} />
          ))}
        </div>
      </div>

      {/* Browse by Category */}
      <div className="mb-8">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-2xl font-semibold text-gray-900">Browse by Category</h2>
          <button
            onClick={fetchCategories}
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
            disabled={loading}
          >
            {loading ? 'Loading...' : 'Load Categories'}
          </button>
        </div>

        {Object.keys(categories).length > 0 && (
          <div className="space-y-6">
            {Object.entries(categories).map(([category, skills]) => (
              <div key={category} className="border rounded-lg p-4">
                <h3 className="text-lg font-semibold text-gray-900 mb-3">
                  {category} ({skills.length} skills)
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2">
                  {skills.slice(0, 6).map(skill => (
                    <SkillCard key={skill.id} skill={skill} />
                  ))}
                </div>
                {skills.length > 6 && (
                  <button className="mt-3 text-blue-500 hover:text-blue-700 text-sm">
                    Show all {skills.length} skills in {category}
                  </button>
                )}
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Quick Add Popular Skills */}
      <div className="bg-gray-50 rounded-lg p-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-3">Quick Add Popular Skills</h3>
        <div className="flex flex-wrap gap-2">
          {['JavaScript', 'Python', 'React', 'Node.js', 'TypeScript', 'AWS', 'Docker', 'MongoDB'].map(skillName => {
            const skill = popularSkills.find(s => s.name === skillName);
            return skill ? (
              <button
                key={skill.id}
                onClick={() => addSkillToUser(skill.id)}
                disabled={isSkillAdded(skill.id)}
                className={`px-3 py-1 rounded-full text-sm ${
                  isSkillAdded(skill.id)
                    ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                    : 'bg-blue-100 text-blue-700 hover:bg-blue-200'
                }`}
              >
                {isSkillAdded(skill.id) ? '✓ Added' : `+ ${skillName}`}
              </button>
            ) : null;
          })}
        </div>
      </div>
    </div>
  );
};

export default SkillsBrowser;