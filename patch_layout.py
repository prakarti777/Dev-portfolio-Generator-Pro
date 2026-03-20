import sys

with open('c:\\Users\\praka\\Downloads\\dev\\dev-portfolio-generator\\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = "// --- PORTFOLIO COMPONENTS ---"
end_marker = "// --- MAIN APP ---"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found!")
    sys.exit(1)

new_components = """// --- PORTFOLIO COMPONENTS ---
        const secClass = "transition-all duration-300 relative z-10 hover:z-20 border border-transparent overflow-hidden";
        
        const P_Hero = ({ data, config, global }) => config.visible && (
            <section class={secClass} style={secStyle(config, global.primary)}>
                {/* Decorative Elements */}
                <div class="absolute top-10 right-10 w-6 h-6 rounded-full opacity-30" style={{backgroundColor: global.primary}}></div>
                <div class="absolute bottom-20 left-10 w-8 h-8 rounded-tr-full rounded-tl-full opacity-40 transform rotate-45" style={{backgroundColor: global.primary}}></div>
                
                <div class="max-w-7xl mx-auto px-6 flex flex-col-reverse md:flex-row items-center gap-12 py-10">
                    <div class="flex-1 text-center md:text-left relative z-10">
                        <div class="inline-block px-4 py-1.5 rounded-full mb-6 text-sm font-bold tracking-widest uppercase shadow-sm" style={{backgroundColor: 'color-mix(in srgb, ' + global.primary + ' 20%, transparent)', color: global.primary}}>
                            {data.title}
                        </div>
                        <h1 class="text-5xl md:text-7xl font-extrabold mb-6 tracking-tight leading-tight">
                            Hello, I Am <br/> <span style={{color: global.primary}}>{data.name}</span>
                        </h1>
                        <p class="text-lg md:text-xl tint-text max-w-xl leading-relaxed mb-10 mx-auto md:mx-0">{data.tagline}</p>
                        <div class="flex flex-wrap justify-center md:justify-start gap-4 items-center">
                            <a href="#contact" style={{backgroundColor: global.primary, color: config.isCustomColorEnabled ? config.backgroundColor : global.bg}} class="px-8 py-4 rounded-full font-bold shadow-xl hover:-translate-y-1 hover:shadow-2xl transition-all">Hire Me</a>
                            <a href="#projects" class="px-6 py-4 font-bold hover:underline transition underline-offset-4" style={{color: config.isCustomColorEnabled ? config.textColor : global.text}}>See My Work ↗</a>
                        </div>
                    </div>
                    <div class="flex-1 relative flex justify-center py-10 w-full">
                        {/* Background Blob */}
                        <div class="absolute inset-0 z-0 m-auto w-full max-w-md aspect-square rounded-full transition-all duration-500 blur-3xl opacity-20" style={{backgroundColor: global.primary}}></div>
                        {/* Solid Offset Arch/Blob */}
                        <div class="absolute bottom-0 md:right-0 w-3/4 h-3/4 rounded-full z-0 opacity-80" style={{backgroundColor: global.primary}}></div>
                        
                        {data.image?.data ? 
                            <img src={data.image.data} alt="Profile" class="w-64 h-64 md:w-96 md:h-96 lg:w-[450px] lg:h-[450px] rounded-[3rem] object-cover relative z-10 shadow-2xl border-8" style={{borderColor: config.isCustomColorEnabled ? config.backgroundColor : global.bg}} />
                            : <div class="w-64 h-64 md:w-96 md:h-96 rounded-[3rem] relative z-10 shadow-2xl border-8 flex items-center justify-center text-4xl" style={{borderColor: config.isCustomColorEnabled ? config.backgroundColor : global.bg, backgroundColor: 'color-mix(in srgb, currentColor 5%, transparent)'}}>👨‍💻</div>
                        }
                    </div>
                </div>
            </section>
        );

        const P_About = ({ data, config, global }) => config.visible && (
            <section id="about" class={secClass} style={secStyle(config, global.primary)}>
                <div class="max-w-6xl mx-auto px-6 flex flex-col md:flex-row gap-12 items-center">
                    <div class="flex-1 relative w-full">
                         <div class="absolute -top-4 -left-4 w-full h-full rounded-[2rem] border-4 opacity-30 pointer-events-none" style={{borderColor: global.primary}}></div>
                         <div class="p-8 md:p-12 rounded-[2rem] tint-card backdrop-blur-sm relative z-10 shadow-xl text-center md:text-left">
                             <h3 class="text-3xl font-bold mb-6" style={{color: global.primary}}>About Me</h3>
                             <p class="text-lg leading-relaxed tint-text whitespace-pre-wrap">{data}</p>
                         </div>
                    </div>
                </div>
            </section>
        );

        const P_Skills = ({ data, config, global }) => config.visible && (
            <section id="skills" class={secClass} style={secStyle(config, global.primary)}>
                <div class="max-w-6xl mx-auto px-6">
                    <div class="text-center mb-16 relative">
                        <span class="text-sm font-bold uppercase tracking-widest mb-2 block" style={{color: global.primary}}>My Expertise</span>
                        <h3 class="text-4xl md:text-5xl font-extrabold leading-tight">Provide Wide Range of <br/> Digital Services</h3>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                        {['languages', 'frameworks', 'tools'].map(cat => (
                            <div key={cat} class="tint-card p-8 rounded-[2rem] shadow-lg hover:-translate-y-2 hover:shadow-2xl transition-all duration-300 relative overflow-hidden group flex flex-col items-center md:items-start text-center md:text-left border border-[color-mix(in_srgb,currentColor_5%,transparent)]">
                                <div class="w-20 h-20 rounded-2xl mb-8 flex items-center justify-center text-4xl shadow-md transition-colors duration-500" style={{backgroundColor: 'color-mix(in srgb, ' + global.primary + ' 15%, transparent)', color: global.primary}}>
                                    {cat === 'languages' ? '💻' : cat === 'frameworks' ? '⚛️' : '🛠️'}
                                </div>
                                <h4 class="font-bold text-2xl capitalize mb-4 relative z-10">{cat}</h4>
                                <div class="flex flex-wrap justify-center md:justify-start gap-2 relative z-10">
                                    {(data[cat]||'').split(',').map((s,i) => s.trim() ? <span key={i} class="tint-card px-4 py-2 rounded-xl text-sm font-bold shadow-sm">{s.trim()}</span> : null)}
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </section>
        );

        const P_Projects = ({ data, config, global }) => config.visible && (
            <section id="projects" class={secClass} style={secStyle(config, global.primary)}>
                <div class="absolute inset-0 z-0 opacity-10 blur-3xl rounded-full max-w-lg mx-auto transform translate-y-32" style={{backgroundColor: global.primary}}></div>
                <div class="max-w-7xl mx-auto px-6 relative z-10">
                    <div class="text-center mb-16">
                         <span class="text-sm font-bold uppercase tracking-widest mb-2 block" style={{color: global.primary}}>Creative Works</span>
                         <h3 class="text-4xl md:text-5xl font-extrabold">Check My Portfolio</h3>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                        {data.map(p => (
                            <div key={p.id} class="tint-card rounded-[2rem] overflow-hidden group shadow-xl hover:-translate-y-2 hover:shadow-2xl transition-all duration-300 flex flex-col border border-[color-mix(in_srgb,currentColor_5%,transparent)]">
                                <div class="h-56 flex items-center justify-center p-6 relative overflow-hidden" style={{backgroundImage: `linear-gradient(to bottom right, color-mix(in srgb, ${global.primary} 20%, transparent), transparent)`}}>
                                     <h4 class="text-3xl font-black text-center relative z-10 transform group-hover:scale-110 group-hover:-translate-y-2 transition-transform duration-500 drop-shadow-md" style={{color: global.primary}}>{p.title}</h4>
                                </div>
                                <div class="p-8 flex-1 flex flex-col backdrop-blur-sm">
                                    <p class="tint-text leading-relaxed mb-8 whitespace-pre-wrap flex-1">{p.description}</p>
                                    <div class="flex flex-wrap gap-2 mb-8">
                                        {(p.techStack||'').split(',').map((t,i) => t.trim() ? <span key={i} class="text-[10px] font-black uppercase tracking-widest tint-text tint-card px-3 py-1.5 rounded-lg border-0">{t.trim()}</span> : null)}
                                    </div>
                                    <div class="flex gap-4 items-center">
                                        {p.liveLink && <a href={p.liveLink} target="_blank" class="px-6 py-2.5 rounded-full text-sm font-bold shadow-lg hover:shadow-xl hover:-translate-y-0.5 transition-all" style={{backgroundColor: global.primary, color: config.isCustomColorEnabled ? config.backgroundColor : global.bg}}>Live Demo</a>}
                                        {p.githubLink && <a href={p.githubLink} target="_blank" class="text-sm font-bold hover:underline opacity-80 hover:opacity-100 transition-opacity" style={{color: config.isCustomColorEnabled ? config.textColor : global.text}}>GitHub ↗</a>}
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </section>
        );

        const P_Experience = ({ data, config, global }) => config.visible && data.length > 0 && (
            <section id="experience" class={secClass} style={secStyle(config, global.primary)}>
                <div class="max-w-6xl mx-auto px-6">
                    <div class="text-center mb-16">
                        <span class="text-sm font-bold uppercase tracking-widest mb-2 block" style={{color: global.primary}}>Career Path</span>
                        <h3 class="text-4xl font-extrabold">Professional Experience</h3>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        {data.map(exp => (
                            <div key={exp.id} class="tint-card p-8 rounded-[2rem] shadow-lg hover:-translate-y-1 hover:shadow-xl transition-all relative group overflow-hidden border border-[color-mix(in_srgb,currentColor_5%,transparent)]">
                                <div class="absolute top-0 right-0 w-32 h-32 rounded-bl-full flex items-start justify-end p-6 opacity-10 transition-opacity group-hover:opacity-20" style={{backgroundColor: global.primary}}><span class="text-4xl translate-x-4 -translate-y-4 inline-block">💼</span></div>
                                <span class="inline-block px-4 py-1.5 rounded-full text-xs font-bold mb-6 shadow-sm" style={{backgroundColor: 'color-mix(in srgb, ' + global.primary + ' 15%, transparent)', color: global.primary}}>{exp.duration}</span>
                                <h4 class="text-2xl font-bold mb-2">{exp.role}</h4>
                                <h5 class="opacity-60 font-black uppercase tracking-widest text-xs mb-6">{exp.company}</h5>
                                <p class="tint-text leading-relaxed whitespace-pre-wrap relative z-10">{exp.description}</p>
                            </div>
                        ))}
                    </div>
                </div>
            </section>
        );

        const P_Certifications = ({ data, config, global }) => config.visible && data.length > 0 && (
            <section id="certifications" class={secClass} style={secStyle(config, global.primary)}>
                <div class="max-w-6xl mx-auto px-6">
                    <div class="text-center mb-16">
                        <span class="text-sm font-bold uppercase tracking-widest mb-2 block" style={{color: global.primary}}>Achievements</span>
                        <h3 class="text-4xl font-extrabold">Certifications</h3>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        {data.map(cert => (
                            <div key={cert.id} class="tint-card rounded-[2rem] overflow-hidden flex flex-col md:flex-row hover:-translate-y-2 transition-all duration-300 shadow-lg hover:shadow-2xl group border border-[color-mix(in_srgb,currentColor_5%,transparent)]">
                                {cert.file?.isImage ? (
                                    <div class="w-full md:w-1/3 h-48 md:h-auto shrink-0 overflow-hidden relative" style={{backgroundColor: 'color-mix(in srgb, currentColor 5%, transparent)'}}>
                                        <div class="absolute inset-0 bg-black/20 group-hover:bg-transparent transition duration-300 z-10"></div>
                                        <img src={cert.file.data} class="w-full h-full object-cover group-hover:scale-110 transition duration-500 relative z-0" />
                                    </div>
                                ) : (
                                    <div class="w-full md:w-1/3 h-48 md:h-auto shrink-0 flex items-center justify-center text-5xl opacity-80" style={{backgroundImage: `linear-gradient(to bottom right, color-mix(in srgb, ${global.primary} 30%, transparent), transparent)`}}>🎓</div>
                                )}
                                <div class="p-8 flex-1 flex flex-col justify-center relative bg-transparent">
                                    <h4 class="text-xl font-bold mb-2 relative z-10">{cert.name}</h4>
                                    <div class="flex flex-col md:flex-row md:items-center gap-2 md:gap-4 mb-4 relative z-10">
                                        <h5 class="font-black uppercase tracking-widest text-xs" style={{color: global.primary}}>{cert.issuer}</h5>
                                        <span class="text-[10px] font-mono tint-card px-2 py-1 rounded-md border-0">{cert.date}</span>
                                    </div>
                                    <p class="tint-text text-sm leading-relaxed whitespace-pre-wrap flex-1 mb-6 relative z-10">{cert.description}</p>
                                    
                                    {cert.file && !cert.file.isImage && (
                                        <a href={cert.file.data} download={cert.file.name} class="mt-auto pl-0 text-xs font-bold uppercase tracking-widest hover:translate-x-1 transition-transform inline-block w-fit" style={{color: global.primary}}>Download Doc →</a>
                                    )}
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </section>
        );

        const P_Education = ({ data, config, global }) => config.visible && data.length > 0 && (
            <section id="education" class={secClass} style={secStyle(config, global.primary)}>
                <div class="max-w-6xl mx-auto px-6">
                    <div class="text-center mb-16">
                        <span class="text-sm font-bold uppercase tracking-widest mb-2 block" style={{color: global.primary}}>Academics</span>
                        <h3 class="text-4xl font-extrabold">Education</h3>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        {data.map(edu => (
                            <div key={edu.id} class="tint-card p-8 rounded-[2rem] flex flex-col sm:flex-row justify-between sm:items-center gap-6 hover:-translate-y-1 hover:shadow-xl transition-all shadow-md border border-[color-mix(in_srgb,currentColor_5%,transparent)]">
                                <div>
                                    <h4 class="text-xl font-bold mb-1">{edu.degree}</h4>
                                    <h5 class="tint-text font-medium text-sm">{edu.institution}</h5>
                                </div>
                                <span class="tint-card border-0 px-4 py-2 rounded-xl text-xs font-black uppercase tracking-widest inline-block text-center shadow-inner whitespace-nowrap">{edu.year}</span>
                            </div>
                        ))}
                    </div>
                </div>
            </section>
        );

        const P_Contact = ({ data, config, global }) => config.visible && (
            <section id="contact" class={secClass} style={secStyle(config, global.primary)}>
                <div class="max-w-6xl mx-auto px-6">
                    <div class="text-center mb-16">
                        <span class="text-sm font-bold uppercase tracking-widest mb-2 block" style={{color: global.primary}}>Get In Touch</span>
                        <h3 class="text-4xl md:text-5xl font-extrabold pb-2">Any Questions? <br/>Feel Free to Contact</h3>
                    </div>
                    <div class="flex flex-col lg:flex-row shadow-2xl rounded-[3rem] overflow-hidden tint-card border border-[color-mix(in_srgb,currentColor_5%,transparent)]">
                        {/* LEFT SIDE */}
                        <div class="lg:w-2/5 p-12 flex flex-col justify-center relative overflow-hidden text-white" style={{backgroundColor: global.primary}}>
                            <div class="absolute top-0 right-0 w-64 h-64 rounded-full filter blur-3xl opacity-50" style={{backgroundColor: 'rgba(255,255,255,0.2)', transform: 'translate(30%, -30%)'}}></div>
                            <div class="absolute bottom-0 left-0 w-48 h-48 rounded-full filter blur-3xl opacity-50" style={{backgroundColor: 'rgba(255,255,255,0.2)', transform: 'translate(-30%, 30%)'}}></div>
                            
                            <h4 class="text-3xl font-black mb-10 relative z-10 tracking-tight">Contact Info</h4>
                            <div class="space-y-8 relative z-10">
                                {data.email && (
                                    <div class="flex items-center gap-6 group hover:translate-x-2 transition-transform">
                                        <div class="w-14 h-14 rounded-2xl bg-white/20 flex items-center justify-center text-xl shadow-inner group-hover:bg-white/30 transition-colors">✉️</div>
                                        <div>
                                            <p class="text-[10px] opacity-70 uppercase tracking-widest mb-1 font-bold">Email</p>
                                            <a href={`mailto:${data.email}`} class="font-bold text-lg hover:opacity-80 transition-opacity">{data.email}</a>
                                        </div>
                                    </div>
                                )}
                                {data.linkedin && (
                                    <div class="flex items-center gap-6 group hover:translate-x-2 transition-transform">
                                        <div class="w-14 h-14 rounded-2xl bg-white/20 flex items-center justify-center text-xl shadow-inner group-hover:bg-white/30 transition-colors">🔗</div>
                                        <div>
                                            <p class="text-[10px] opacity-70 uppercase tracking-widest mb-1 font-bold">LinkedIn</p>
                                            <a href={data.linkedin} target="_blank" class="font-bold text-lg hover:opacity-80 transition-opacity whitespace-nowrap overflow-hidden text-ellipsis max-w-[200px] block">View Profile</a>
                                        </div>
                                    </div>
                                )}
                                {data.github && (
                                    <div class="flex items-center gap-6 group hover:translate-x-2 transition-transform">
                                        <div class="w-14 h-14 rounded-2xl bg-white/20 flex items-center justify-center text-xl shadow-inner group-hover:bg-white/30 transition-colors">💻</div>
                                        <div>
                                            <p class="text-[10px] opacity-70 uppercase tracking-widest mb-1 font-bold">GitHub</p>
                                            <a href={data.github} target="_blank" class="font-bold text-lg hover:opacity-80 transition-opacity">View Profile</a>
                                        </div>
                                    </div>
                                )}
                            </div>
                        </div>
                        {/* RIGHT SIDE */}
                        <div class="lg:w-3/5 p-12 md:p-16 flex flex-col justify-center">
                            <form class="space-y-6" onSubmit={e=>e.preventDefault()}>
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                                    <input type="text" placeholder="Your Name" class="w-full border-none rounded-2xl px-6 py-4 focus:outline-none focus:ring-2 transition-all shadow-inner tint-card" style={{color: config.isCustomColorEnabled ? config.textColor : global.text, '--tw-ring-color': global.primary}} />
                                    <input type="email" placeholder="Your Email" class="w-full border-none rounded-2xl px-6 py-4 focus:outline-none focus:ring-2 transition-all shadow-inner tint-card" style={{color: config.isCustomColorEnabled ? config.textColor : global.text, '--tw-ring-color': global.primary}} />
                                </div>
                                <input type="text" placeholder="Subject" class="w-full border-none rounded-2xl px-6 py-4 focus:outline-none focus:ring-2 transition-all shadow-inner tint-card" style={{color: config.isCustomColorEnabled ? config.textColor : global.text, '--tw-ring-color': global.primary}} />
                                <textarea placeholder="Message" rows="5" class="w-full border-none rounded-2xl px-6 py-4 focus:outline-none focus:ring-2 transition-all shadow-inner resize-none tint-card" style={{color: config.isCustomColorEnabled ? config.textColor : global.text, '--tw-ring-color': global.primary}}></textarea>
                                <button class="px-10 py-4 rounded-full font-bold shadow-xl hover:-translate-y-1 hover:shadow-2xl transition-all" style={{backgroundColor: global.primary, color: config.isCustomColorEnabled ? config.backgroundColor : global.bg}}>Submit Message</button>
                            </form>
                        </div>
                    </div>
                </div>
            </section>
        );

        const P_Footer = ({ heroData, config, global }) => config.visible && (
            <footer class={secClass + " border-t border-[color-mix(in_srgb,currentColor_15%,transparent)]"} style={{...secStyle(config, global.primary), backgroundColor: 'color-mix(in srgb, currentColor 2%, transparent)', backdropFilter: 'blur(10px)'}}>
                <div class="max-w-6xl mx-auto px-6 py-10 flex flex-col md:flex-row items-center justify-between gap-6 text-center md:text-left">
                    <div class="flex items-center gap-3">
                        <div class="w-8 h-8 rounded-full flex items-center justify-center text-xs font-black shadow-md" style={{backgroundColor: global.primary, color: config.isCustomColorEnabled ? config.backgroundColor : global.bg}}>{heroData.name.charAt(0)}</div>
                        <h4 class="font-extrabold tracking-widest uppercase">{heroData.name}</h4>
                    </div>
                    <ul class="flex flex-wrap items-center justify-center gap-6 text-sm font-bold opacity-70">
                        <li><a href="#about" class="hover:opacity-100 transition">About</a></li>
                        <li><a href="#skills" class="hover:opacity-100 transition">Skills</a></li>
                        <li><a href="#projects" class="hover:opacity-100 transition">Portfolio</a></li>
                        <li><a href="#contact" class="hover:opacity-100 transition">Contact</a></li>
                    </ul>
                    <p class="text-xs font-medium opacity-50">&copy; {new Date().getFullYear()} All Rights Reserved.</p>
                </div>
            </footer>
        );
"""

text = text[:start_idx] + new_components + text[end_idx:]

with open('c:\\Users\\praka\\Downloads\\dev\\dev-portfolio-generator\\index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Patch successfully applied!")
